import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import environ
import smtplib

load_dotenv()

STOCK = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = environ.get("STOCK_KEY")
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_KEY,
}

COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = environ.get("NEWS_KEY")
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_KEY,
    "language": "es",
    "pageSize": 3,
}

MY_EMAIL = environ.get("MY_EMAIL")
MY_PASSWORD = environ.get("MY_EMAIL_PASSWORD")


def stock_change():
    now = datetime.now()
    yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    before_yesterday = (now - timedelta(days=2)).strftime("%Y-%m-%d")
    response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
    response.raise_for_status()
    stock_data = response.json()
    daily_data = stock_data["Time Series (Daily)"]

    yesterday_close = float(daily_data[yesterday]["4. close"])
    before_close = float(daily_data[before_yesterday]["4. close"])
    diff = round(yesterday_close - before_close, 2)
    percentage = round((diff / yesterday_close) * 100, 2)

    return percentage


def get_news():
    response = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data["articles"]

    return articles


ch_percent = stock_change()

if abs(ch_percent) >= 5:
    emoji = "🔺" if ch_percent > 0 else "🔻"
    stock_text = STOCK + ": " + emoji + f"{abs(ch_percent)}%\n"
    news = get_news()
    for article in news:
        headline = "Headline: " + article["title"] + "\n"
        brief = "Brief: " + article["description"].strip()

        subject = "Subject:" + stock_text + "\n\n"
        message = subject + headline + brief
        message = message.encode('ascii', 'ignore')

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=message
            )
