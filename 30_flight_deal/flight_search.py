import requests
from os import environ
from dotenv import load_dotenv
from flight_data import FlightData
from datetime import datetime, timedelta

load_dotenv()
TRAVEL_FROM = "LCY"  # London
TRAVEL_KEY = environ.get("TRAVEL_KEY")
TRAVEL_SECRET = environ.get("TRAVEL_SECRET")
TRAVEL_ENDPOINT = environ.get("TRAVEL_ENDPOINT")
V2_ENDPOINT = environ.get("DEAL_ENDPOINT")

OAUTH_ENDPOINT = f"{TRAVEL_ENDPOINT}/security/oauth2/token"
OFFER_ENPOINT = f"{V2_ENDPOINT}/shopping/flight-offers"

IATA_ENDPOINT = f"{TRAVEL_ENDPOINT}/reference-data/locations/cities"


class FlightSearch:

    def __init__(self) -> None:
        self.deals: list[FlightData] = []
        self.token = self.get_token()

    def get_token(self):
        oauth_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        oauth_body = {
            "grant_type": "client_credentials",
            "client_id": TRAVEL_KEY,
            "client_secret": TRAVEL_SECRET,
        }
        oauth_response = requests.post(
            OAUTH_ENDPOINT,
            headers=oauth_headers,
            data=oauth_body,
        )
        oauth_response.raise_for_status()
        oauth_data = oauth_response.json()
        token = oauth_data["token_type"] + " " + oauth_data["access_token"]
        return token

    def get_city_iata(self, city_name: str):
        headers = {
            "Authorization": self.token,
        }
        params = {
            "keyword": city_name
        }
        response = requests.get(
            IATA_ENDPOINT,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        city_iata = response.json()["data"][0]["iataCode"]
        self.set_flight_data(city_iata)
        return city_iata

    def set_flight_data(self, city: str):
        new_flight_data = FlightData(city)
        data = self.find_deal(new_flight_data)
        self.deals.append(data)

    def find_deal(self, data: FlightData):
        headers = {
            "Authorization": self.token,
        }
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        return_date = (
            datetime.now() + timedelta(weeks=24)
        ).strftime("%Y-%m-%d")

        params = {
            "originLocationCode": TRAVEL_FROM,
            "destinationLocationCode": data.city,
            "departureDate": tomorrow,
            "returnDate": return_date,
            "adults": 1,
            "currencyCode": "USD",
        }
        response = requests.get(
            OFFER_ENPOINT,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        new_data = response.json()["data"]
        for row in new_data:
            data.set_lower_price(row, tomorrow, return_date)

        return data

    def get_lower_price(self, city: str):
        for data in self.deals:
            if data.city == city:
                return data
