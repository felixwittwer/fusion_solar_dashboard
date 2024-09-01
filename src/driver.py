# file: driver.py
# This file is used to start the selenium driver and open the website.
# (c)2024 Felix Wittwer

import src.settings as st
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException

def get_driver():
    try:
        if st.HEADLESS:
            if st.SELENIUM_BROWSER == "FIREFOX":
                options = FirefoxOptions()
                options.add_argument("--headless")
            elif st.SELENIUM_BROWSER == "CHROME":
                options = ChromeOptions()
                options.add_argument("--headless")
        if st.SELENIUM_BROWSER == "FIREFOX":
            driver = webdriver.Firefox(options=options)
        elif st.SELENIUM_BROWSER == "CHROME":
            driver = webdriver.Chrome(options=options)

        driver.set_window_size(st.WINDOW_WIDTH, st.WINDOW_HEIGHT)
        return driver
    except WebDriverException:
        print("get_driver WebDriverException")
    except:
        print("get_driver another exception accured")
