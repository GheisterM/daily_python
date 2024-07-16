import requests
from os import environ
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

HOST_DOMAIN = "https://trackapi.nutritionix.com"
NL_ENDPOINT = f"{HOST_DOMAIN}/v2/natural/exercise"
NUTRI_HEADERS = {
    "x-app-id": environ.get("APP_ID"),
    "x-app-key": environ.get("APP_KEY"),
}

SHEETY_ENDPOINT = environ.get("SHEETY_ENDPOINT")
SHEETY_HEADER = {
    "Authorization": environ.get("AUTH_TOKEN")
}

nutri_body = {
    "query": input("Tell me what you did today: "),
}
nutri_response = requests.post(
    NL_ENDPOINT,
    headers=NUTRI_HEADERS,
    json=nutri_body
)
nutri_response.raise_for_status()
exercises = nutri_response.json()["exercises"]

sheety_body = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%I:%M:%S %p"),
        "exercise": ", ".join(
            [exercise["name"].title() for exercise in exercises]
        ),
        "duration": sum(
            [exercise["duration_min"] for exercise in exercises]
        ),
        "calories": sum(
            [exercise["nf_calories"] for exercise in exercises]
        ),
    }
}
sheety_response = requests.post(
    SHEETY_ENDPOINT,
    headers=SHEETY_HEADER,
    json=sheety_body
)
sheety_response.raise_for_status()
print(sheety_response.text)
