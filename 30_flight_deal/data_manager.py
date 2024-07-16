import requests
from os import environ
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    def __init__(self):
        self.endpoint = environ.get("SHEET_ENDPOINT")
        self.users_endpoint = environ.get("USERS_ENDPOINT")
        self.headers = {
            "Authorization": environ.get("SHEET_TOKEN")
        }
        self.prices: list[dict] = []
        self.users: list[dict] = []
        self.get_prices()
        self.get_users()

    def get_prices(self):
        response = requests.get(self.endpoint, headers=self.headers)
        response.raise_for_status()
        self.prices = response.json()["prices"]

    def update_iata(self, data: dict):
        body = {
            "price": {
                "city": data["city"],
                "iataCode": data["iataCode"],
                "lowestPrice": data["lowestPrice"],
            }
        }
        put_endpoint = self.endpoint + f"/{data['id']}"
        response = requests.put(
            put_endpoint,
            headers=self.headers,
            json=body
        )
        response.raise_for_status()
        self.get_prices()

    def get_users(self):
        response = requests.get(self.users_endpoint, headers=self.headers)
        response.raise_for_status()
        self.users = response.json()["users"]
