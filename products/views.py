import requests
from django.http.response import HttpResponse
from .tasks import fetch_data_from_flexibee_api, add
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def index(request):
    auth = (os.getenv("FLEXB_USER"), os.getenv("FLEXB_PASS"))
    response = requests.get("https://sas-technologi.flexibee.eu:5434/c/einteriors_s_r_o_/cenik.json?detail=custom:id&limit=1&order=id@D", auth=auth)
    data = response.json()['winstrom']['cenik']

    max_id = data[0]["id"]

    for id_value in range(1, int(max_id) + 1):
        url = f"https://sas-technologi.flexibee.eu:5434/c/einteriors_s_r_o_/cenik/{id_value}.json?detail=custom:id,kod,nazev,exportNaEshop,prilohy(nazSoub,%20content,%20link,%20typK)&relations=prilohy"
        fetch_data_from_flexibee_api.delay(url)

    return HttpResponse("Urls sent")

def add_task(request):
    result = add.delay(2, 3)

    try:
        result_value = result.get(timeout=10)
    except TimeoutError:
        result_value = "Timed out"

    return HttpResponse(result_value)