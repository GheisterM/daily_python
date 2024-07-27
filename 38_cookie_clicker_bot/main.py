from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from time import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

start = time()
current_time = 0
time_limit = 60 * 5

while current_time < time_limit:
    cookie.click()
    current_time = time() - start
    if round(current_time) % 5 == 0:
        can_buy = True
        while can_buy:
            try:
                upgrade = driver.find_elements(
                    By.CSS_SELECTOR,
                    value="#store div"
                )
                upgrade = upgrade[::-1]
                available_upgrade = [upgrade for upgrade in upgrade
                                     if upgrade.get_attribute("class") == ""]
                can_buy = len(available_upgrade) > 0
                if can_buy:
                    print(available_upgrade[0].get_attribute("id"))
                    available_upgrade[0].click()
            except StaleElementReferenceException:
                print("Must wait for refresh.")
                pass

print(money.text)
driver.quit()
