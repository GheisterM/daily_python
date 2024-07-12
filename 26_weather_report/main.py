import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_KEY = os.environ.get("OWM_KEY")

MY_EMAIL = os.environ.get("MY_EMAIL")
print(MY_EMAIL)
MY_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
EMAIL_SUBJECT = "Subject:Weather Report\n\n"

weather_params = {
    "lat": 7.131180,
    "lon": -73.125031,
    "appid": OWM_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_list = response.json()["list"]
rain_times = [item["dt_txt"] for item in weather_list
              if item["weather"][0]["id"] < 700]

if len(rain_times) > 0:
    message = "There's rain expected for the following hours:\n"
    message += "\n".join(rain_times)
    message += "\nBring an umbrella!"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, EMAIL_SUBJECT + message)
