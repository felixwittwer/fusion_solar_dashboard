# file: routines.py
# This file is used to define the different routines that can be executed by the selenium_solar_data.py file.
# (c)2024 Felix Wittwer

from src.parts import open_page
from src.parts import fetch_data
from src.parts import create_site
from src.utils import screenshot

def standard(driver):
    open_page.main(driver)
    fetch_data.main(driver, True)
    create_site.main()
    return driver

def full(driver):
    open_page.main(driver)
    fetch_data.main(driver, True)
    create_site.main()
    screenshot(driver)
    return driver

def create_dashboard_from_csv(driver):
    create_site.main()
    return driver

def screenshot_main_page(driver):
    open_page.main(driver)
    screenshot(driver)
    return driver
