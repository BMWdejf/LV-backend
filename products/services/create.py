#from .base import fetch_data_from_flexibee_api
from products.models import Products
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

# Create products from Flexibee API
def create_product(row):
    try:
        prilohy_link = None
        if 'prilohy' in row and row['prilohy']:
            prilohy_link = row['prilohy'][0]['link']

        export_na_eshop = row.get('exportNaEshop')

        if export_na_eshop:
            export_na_eshop = str2bool(export_na_eshop)
        else:
            export_na_eshop = False

        Products.objects.create(
            fx_id=row['id'],
            code=row['kod'],
            name=row['nazev'],
            img_link=prilohy_link,
            export_on_eshop=export_na_eshop,
        )
        logging.info(f"Product with ID {row['id']} created")
    except Exception as e:
        logging.error(f"Error creating products from API: {e}")
