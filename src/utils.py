# file: utils.py
# This file is the home of all utility functions. E.g. the screenshot function.
# (c)2024 Felix Wittwer

import os
from datetime import datetime

def screenshot(driver):
    if not os.path.isdir('./screenshots/'):
        os.makedirs('./screenshots/')
    time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.save_screenshot(f'./screenshots/screenshot_{time}.png')
