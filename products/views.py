<<<<<<< HEAD
from products.models import Products
import requests
from os import getenv


def get_flexibee_data(start_id=1, end_id=100):
    for id in range(start_id, end_id + 1):
        url = f"https://sas-technologi.flexibee.eu:5434/c/einteriors_s_r_o_/cenik/{id}.json?detail=custom:id,kod,nazev,exportNaEshop,prilohy(nazSoub,%20content,%20link,%20typK)&relations=prilohy"
        auth = (getenv("FLEXB_USER"), getenv("FLEXB_PASS"))
        response = requests.get(url, auth=auth)
        data = response.json()['winstrom']['cenik']

        for row in data:
            prilohy_link = None
            if 'prilohy' in row and row['prilohy']:
                prilohy_link = row['prilohy'][0]['link']

            export_on_eshop = True if row['exportNaEshop'].lower() == "true" else False

            existing_record = Products.objects.filter(fx_id=row['id']).exists()

            print(f"Záznam v databazi: {existing_record}, záznam v JSON souboru: {row['exportNaEshop']}")

            if not existing_record and export_on_eshop:
                # Přidat záznam, pokud neexistuje a exportNaEshop je true
                Products.objects.create(
                    fx_id=row['id'],
                    code=row['kod'],
                    name=row['nazev'],
                    img_link=prilohy_link,
                    exportNaEshop=export_on_eshop
                )
                print(f"Data from {id}.json saved to database")
            elif existing_record and not export_on_eshop:
                # Pokud záznam existuje a exportNaEshop je false, aktualizujte
                Products.objects.filter(fx_id=row['id']).update(
                    code=row['kod'],
                    name=row['nazev'],
                    img_link=prilohy_link,
                    exportNaEshop=export_on_eshop
                )
                print(f"Data from {id}.json updated in the database")
            elif existing_record and export_on_eshop:
                # Pokud záznam existuje a exportNaEshop je true, přeskočit aktualizaci
                print(f"Data from {id}.json skipped (record exists and exportNaEshop is true)")
            else:
                # Aktualizovat záznam, pokud již existuje a exportNaEshop je false nebo není uvedeno
                Products.objects.filter(fx_id=row['id']).update(
                    code=row['kod'],
                    name=row['nazev'],
                    img_link=prilohy_link,
                    exportNaEshop=export_on_eshop
                )
        print(f"Data from {id}.json saved to database")

=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 328f7f1 (Install clean Django app "Products")
