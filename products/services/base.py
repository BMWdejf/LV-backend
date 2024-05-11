import requests
from os import getenv

def fetch_data_from_flexibee_api(start_id=1, end_id=100):
    data_list = []
    for id in range(start_id, end_id + 1):
        url = f"https://sas-technologi.flexibee.eu:5434/c/einteriors_s_r_o_/cenik/{id}.json?detail=custom:id,kod,nazev,exportNaEshop,prilohy(nazSoub,%20content,%20link,%20typK)&relations=prilohy"
        auth = (getenv("FLEXB_USER"), getenv("FLEXB_PASS"))
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            data = response.json()['winstrom']['cenik']
            data_list.extend(data)
        else:
            print(f"Failed to fetch data from API for ID: {id}")
    return data_list
