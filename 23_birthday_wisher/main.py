import datetime as dt
import smtplib
import os
import pandas
import random

EMAIL_FROM = "example@gmail.com"
EMAIL_PASS = "yourpass"
EMAIL_SUBJECT = "Subject:Happy Birthday!\n\n"

TEMPLATE_PATH = "23_birthday_wisher/letter_templates"
templates = [x for x in os.listdir(TEMPLATE_PATH)
             if os.path.isfile(TEMPLATE_PATH + '/' + x)]

DATA_PATH = "23_birthday_wisher/birthdays.csv"
birthdays = pandas.read_csv(DATA_PATH)

today = dt.datetime.now()
today_birthdays = birthdays[(birthdays["month"] == today.month)
                            & (birthdays["day"] == today.day)]

if len(templates) > 0:
    for birthday in today_birthdays.itertuples():
        to_name = birthday.name
        to_email = birthday.email
        letter = random.choice(templates)
        message = ""
        try:
            with open(TEMPLATE_PATH + "/" + letter) as file:
                message = file.read().replace("[NAME]", to_name)
        except FileNotFoundError:
            message = f"Happy birthday {to_name}!"

        final_message = EMAIL_SUBJECT + message

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_FROM, password=EMAIL_PASS)
            connection.sendmail(EMAIL_FROM, to_email, final_message)
