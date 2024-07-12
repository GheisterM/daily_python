import requests
from datetime import datetime
import math
import smtplib
from time import sleep

ISS_URL = "http://api.open-notify.org/iss-now.json"
MY_LAT = -37.3768  # Your latitude
MY_LONG = -17.6646  # Your longitude
SUN_URL = "https://api.sunrise-sunset.org/json"
MY_EMAIL = "example@gmail.com"
MY_PASS = "yourpassword"
SUBJECT = "Subject:Look up!\n\n"
MESSAGE = "ISS is above you right now, look up!"


def iss_near():
    response = requests.get(url=ISS_URL)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    my_loc = [MY_LAT, MY_LONG]
    iss_loc = [iss_latitude, iss_longitude]
    distance = math.dist(my_loc, iss_loc)

    return distance >= -5 and distance <= 5


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(SUN_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now < sunrise or hour_now > sunset:
        return True

    return False


while True:
    if iss_near() and is_dark():
        with smtplib.SMTP("smtp.google.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=SUBJECT+MESSAGE
            )

    sleep(60)
