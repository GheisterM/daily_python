import smtplib
from os import environ
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

MY_EMAIL = environ.get("MY_EMAIL")
MY_PASSWORD = environ.get("MY_EMAIL_PASSWORD")
MESSAGE = """
Low price alert! Only {}$ to fly from {} to {} with {} stops.
Departing on {} and returning on {}.
"""


class NotificationManager:

    def __init__(self):
        pass

    def send_message(self, data: FlightData, to_email: str):
        subject = f"Subject:Deal found for flight to {data.city}\n\n"
        msg_body = MESSAGE.format(
            data.price,
            data.departure,
            data.destination,
            data.stops,
            data.date_begin,
            data.date_end
        )
        final_msg = subject + msg_body
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=final_msg
            )
