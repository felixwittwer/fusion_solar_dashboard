# file: selenium_solar_data.py
# This file is the main file of the program which gets the driver and runs the full routine.
# (c)2024 Felix Wittwer

from src.driver import get_driver
from src.routines import standard

driver = get_driver()
standard(driver)
driver.close()
