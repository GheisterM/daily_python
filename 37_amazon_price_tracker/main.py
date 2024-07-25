from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from os import environ
import smtplib

load_dotenv()

URL = environ.get("URL")

MY_EMAIL = environ.get("MY_EMAIL")
MY_PASSWORD = environ.get("MY_PASSWORD")
MIN_PRICE = float(environ.get("MIN_PRICE"))

headers = {
    "Accept-Language": "en-US,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}
response = requests.get(URL, headers=headers)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")

price_type = soup.find(name="span", class_="aok-offscreen")

price = "0"
if price_type is not None:
    price = soup.find(name="span", class_="a-price-whole").getText().strip()
    price += soup.find(
        name="span",
        class_="a-price-fraction"
    ).getText().strip()
else:
    price = soup.find(name="span", class_="a-offscreen").getText().strip()
    price = price.replace("US$", "")

price = float(price)

if price <= MIN_PRICE:
    product_name = soup.find(name="span", id="productTitle").getText().strip()
    subject = "Subject:New deal found!\n\n"
    body = f"Your {product_name} price is {price}$, go buy it now!\n{URL}"
    message = subject + body
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, message)
