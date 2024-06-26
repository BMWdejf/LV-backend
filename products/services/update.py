from .base import fetch_data_from_flexibee_api
from products.models import Products
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Create products from Flexibee API
def update_products(row):
    try:
        prilohy_link = None
        if 'prilohy' in row and row['prilohy']:
            prilohy_link = row['prilohy'][0]['link']

        Products.objects.update(
            fx_id=row['id'],
            code=row['kod'],
            name=row['nazev'],
            img_link=prilohy_link,
            export_on_eshop=row.get('export_on_eshop', False)
        )
        logging.info(f"Product with ID {row['id']} created")
    except Exception as e:
        logging.error(f"Error creating products from API: {e}")
