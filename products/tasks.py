from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from os import getenv
from django.db import transaction
from products.models import Products
from products.services.create import create_product
from products.services.update import update_products

logger = get_task_logger(__name__)


@shared_task
def fetch_data_from_flexibee_api(url):
    auth = (getenv("FLEXB_USER"), getenv("FLEXB_PASS"))
    try:
        response = requests.get(url, auth=auth)
        logger.info(response.status_code)
        if response.status_code == 200:
            try:
                with transaction.atomic():
                    data = response.json()['winstrom']['cenik']
                    for item in data:
                        db_item = Products.objects.filter(fx_id=item["id"]).first()
                        if db_item:
                            update_products(item)
                        else:
                            create_product(item)

            except Exception as e:
                #TODO: Add error logging to file or database
                pass
        else:
            #TODO: Add error logging to file or database
            logger.error(f"Failed to fetch data from Flexibee API: {response.status_code}")

    except (KeyError, requests.exceptions.RequestException) as e:
        print(e)

@shared_task()
def add(x, y):
    return x * y