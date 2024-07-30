from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from dotenv import load_dotenv
from os import environ
from time import sleep
import smtplib

load_dotenv()

URL = "https://www.speedtest.net/"
EMAIL = environ.get("EMAIL")
PASSWORD = environ.get("PASSWORD")
ISP_EMAIL = environ.get("ISP_EMAIL")
MIN_DW_SPEED = float(environ.get("MIN_DW_SPEED"))
MIN_UP_SPEED = float(environ.get("MIN_UP_SPEED"))
MESSAGE = """Good day, {}
Why is my internet speed {}down/{}up when I pay for {}down/{}up?"""


class Speedtest:

    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def DoTest(self):
        self.driver.get(URL)

        isp = self.driver.find_element(
            By.CSS_SELECTOR,
            ".ispComponent .result-label"
        )

        start_button = None
        while start_button is None:
            try:
                start_button = self.driver.find_element(
                    By.CLASS_NAME,
                    value="js-start-test"
                )
            except exceptions.NoSuchElementException:
                start_button = None
                sleep(1)

        start_button.click()

        results = None
        while results is None:
            try:
                download = self.driver.find_element(
                    By.CLASS_NAME,
                    value="download-speed"
                )
                upload = self.driver.find_element(
                    By.CLASS_NAME,
                    value="upload-speed"
                )
                results = {
                    "download": float(download.text),
                    "upload": float(upload.text)
                }
            except ValueError:
                results = None
                sleep(3)

        self.CheckSpeed(results, isp.text)

    def CheckSpeed(self, results: dict, isp_name: str):
        subject = "Subject:Service speed problems.\n\n"
        body = MESSAGE.format(
            isp_name,
            results["download"],
            results["upload"],
            MIN_DW_SPEED,
            MIN_UP_SPEED
        )
        message = subject + body

        if (results["download"] < MIN_DW_SPEED
                or results["upload"] < MIN_UP_SPEED):

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.send_message(
                    from_addr=EMAIL,
                    to_addrs=ISP_EMAIL,
                    msg=message
                )

        self.driver.quit()
