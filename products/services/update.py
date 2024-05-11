from .base import fetch_data_from_flexibee_api
from products.models import Products

def update_products_from_api(start_id=1, end_id=100):
    data_list = fetch_data_from_flexibee_api(start_id, end_id)
    for row in data_list:
        prilohy_link = None
        if 'prilohy' in row and row['prilohy']:
            prilohy_link = row['prilohy'][0]['link']

        Products.objects.update_or_create(
            fx_id=row['id'],
            defaults={
                'code': row['kod'],
                'name': row['nazev'],
                'img_link': prilohy_link,
                'export_on_eshop': row.get('export_on_eshop', False)
            }
        )
        print(f"Product with ID {row['id']} updated or created")
