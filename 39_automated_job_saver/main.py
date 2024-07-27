from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import environ
from time import sleep

load_dotenv()

URL = environ.get("URL")
USERNAME = environ.get("EMAIL")
PASSWORD = environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get(URL)

sleep(3)

login_xpath = "/html/body/div[1]/header/nav/div/a[2]"
login_button = driver.find_element(By.XPATH, value=login_xpath)
login_button.click()

sleep(3)

user_field = driver.find_element(By.ID, value="username")
print(USERNAME)
user_field.send_keys(USERNAME)

pass_field = driver.find_element(By.ID, value="password")
pass_field.send_keys(PASSWORD)

submit_button = driver.find_element(
    By.CSS_SELECTOR,
    value=".login__form_action_container button"
)
submit_button.click()

sleep(3)

job_list = driver.find_elements(By.CSS_SELECTOR, value="ul .ember-view a")

for job in job_list:
    job.click()
    sleep(1)
    save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    save_button.click()
    follow_button = driver.find_element(By.CLASS_NAME, value="follow")
    follow_button.click()
    sleep(1)

driver.quit()
