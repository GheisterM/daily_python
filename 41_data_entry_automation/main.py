import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

load_dotenv()

RENTAL_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = environ.get("GOOGLE_FORM")

headers = {
    "Accept-Language": "en-US,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

response = requests.get(RENTAL_URL, headers=headers)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")

addr_tag = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper address")
address = [addr.get_text().replace(" | ", " ").strip() for addr in addr_tag]

prc_tag = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper .PropertyCardWrapper__StyledPriceLine")
prices = [price.get_text().replace("/mo", "").split("+")[0].strip()
          for price in prc_tag]

href_tag = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper .property-card-link")
links = [link.attrs["href"].strip() for link in href_tag]

data = [
    {
        "address": address[i],
        "price": prices[i],
        "link": links[i],
    }
    for i in range(len(links))
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(FORM_URL)

for row in data:
    sleep(1)
    addr_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    addr_button.click()
    addr_button.send_keys(row["address"])
    price_button.click()
    price_button.send_keys(row["price"])
    link_button.click()
    link_button.send_keys(row["link"])
    send_button.click()

    sleep(1)
    reload_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    reload_button.click()

driver.quit()
