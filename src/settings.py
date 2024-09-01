# file: settings.py
# This file is used to set constant variables that are used by the different functions.
# (c)2024 Felix Wittwer

from os import environ

SELENIUM_URL = environ.get("SELENIUM_URL", "") # URL of fusion solar kiosk
SELENIUM_BROWSER = "CHROME" # Browser:"CHROME" or "FIREFOX", currently only Chrome and Firefox are supported
HEADLESS = True # run browser without any graphical interface
WINDOW_WIDTH = 1920 # important for the size of the screenshot
WINDOW_HEIGHT = 1080 # important for the size of the screenshot
MAX_POWER = 25 # in kW
DAY_GOAL= 200 # in kWh
MONTH_GOAL = 6000 # in kWh