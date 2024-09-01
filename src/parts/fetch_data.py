# file: fetch_data.py
# This file is used to fetch data from the website.
# (c)2024 Felix Wittwer

import csv
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

def current_power_and_climate_protection(driver, save):
    top_power_fields = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, '//p[@class="nco-kiosk-overview-data"]')))
    top_power_fields = driver.find_elements(By.XPATH, '//p[@class="nco-kiosk-overview-data"]')
    power_values = []
    for field in range(len(top_power_fields)):
        powerUnit = top_power_fields[field].find_element(By.TAG_NAME, 'span').text
        power_values.append(float(top_power_fields[field].text.replace(powerUnit, '')))
        power_values.append(powerUnit)
    climate_fields = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, '//div[@class="nco-kiosk-social-contribution-content"]')))
    sleep(1) # small wait to guarantee that the page is fully loaded
    co2 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//div[@class="scoial-contribution-item social-co2-item"]')))
    coal = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//div[@class="scoial-contribution-item social-coal-item"]')))
    trees = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//div[@class="scoial-contribution-item social-trees-item"]')))
    co2 = driver.find_element(By.XPATH, '//div[@class="scoial-contribution-item social-co2-item"]').find_element(By.TAG_NAME, 'p')
    co2Unit = co2.find_element(By.TAG_NAME, 'span').text
    coal = driver.find_element(By.XPATH, '//div[@class="scoial-contribution-item social-coal-item"]').find_element(By.TAG_NAME, 'p')
    coalUnit = coal.find_element(By.TAG_NAME, 'span').text
    trees = driver.find_element(By.XPATH, '//div[@class="scoial-contribution-item social-trees-item"]').find_element(By.TAG_NAME, 'p')
    climate_values = [float(co2.text.replace(co2Unit, '')), co2Unit, float(coal.text.replace(coalUnit, '')), coalUnit, trees.text]
    
    if save:
        save_data_to_csv(power_values, climate_values)

    return driver

def save_data_to_csv(power_values, climate_values):
            data = [
                ['current_power', 'current_power_unit', 'today_power', 'today_power_unit','month_power', 'month_power_unit', 'year_power', 'year_power_unit', 'total_power', 'total_power_unit', 'co2', 'co2_unit', 'coal', 'coal_unit', 'tree', 'time'],
                [power_values[0], power_values[1],power_values[2], power_values[3], power_values[4], power_values[5], power_values[6], power_values[7], power_values[8], power_values[9], climate_values[0], climate_values[1], climate_values[2], climate_values[3], climate_values[4], time.strftime("%d.%m.%Y %H:%M", time.localtime())]
            ]

            with open('fetched_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)

def main(driver, save):
    try:
        current_power_and_climate_protection(driver, save)
    except Exception as e:
        print(e)

    return driver
