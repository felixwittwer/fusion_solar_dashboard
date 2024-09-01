# file: open_page.py
# This file is used to start the selenium driver and open the website.
# (c)2024 Felix Wittwer

import src.settings as st
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def main(driver):
    try:
        driver.get(st.SELENIUM_URL)
        top_power_fields = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, '//p[@class="nco-kiosk-overview-data"]')))
        sleep(1) # small wait to guarantee that the page is fully loaded
    except Exception as e:
        print(e)

    return driver
