import requests
from os import getenv
from celery import shared_task
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

@shared_task
def fetch_data_from_flexibee_api():

    # Start from id
    id_value = 1
    # Fetch data from Flexibee API
    data_list = []

    while True:
        url = f"https://sas-technologi.flexibee.eu:5434/c/einteriors_s_r_o_/cenik/{id_value}.json?detail=custom:id,kod,nazev,exportNaEshop,prilohy(nazSoub,%20content,%20link,%20typK)&relations=prilohy"
        auth = (getenv("FLEXB_USER"), getenv("FLEXB_PASS"))
        try:
            response = requests.get(url, auth=auth)
            if response.status_code != 200:
                logging.error(f"Failed to fetch data from Flexibee API: {response.status_code}")
                break
            data = response.json()['winstrom']['cenik']
            data_list.extend(data)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from Flexibee API: {e}")
        except KeyError as e:
            logging.error(f"Error parsing data from Flexibee API: {e}")
        id_value += 1

    return data_list
