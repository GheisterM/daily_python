# import requests
# from os import environ
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv()

sheet = DataManager()
search_manager = FlightSearch()
message_manager = NotificationManager()

for price in sheet.prices:
    if price["iataCode"] == "":
        price["iataCode"] = search_manager.get_city_iata(price["city"])
        sheet.update_iata(price)
    else:
        search_manager.set_flight_data(price["iataCode"])

    lower_price = search_manager.get_lower_price(price["iataCode"])
    if lower_price.price > 0 and lower_price.price < price["lowestPrice"]:
        for user in sheet.users:
            message_manager.send_message(lower_price, user["email"])
