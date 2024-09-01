# file: create_site.py
# This file is used to create a dashboard site by filling in the fetched data into a template dashboard.
# (c)2024 Felix Wittwer

import csv
import src.settings as st
from jinja2 import Environment, FileSystemLoader, select_autoescape

def create_site(**kwargs):
    # Create the dashboard site by filling in the fetched data into a html template.
    envhtml = Environment(
        loader=FileSystemLoader('src/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = envhtml.get_template('/index.html')

    with open('dashboard/dashboard.html', 'w') as file:
        file.write(template.render(**kwargs)) 
    
    # Create the arc diagrams by filling in the fetched data into a js template.
    envjs = Environment(
        loader=FileSystemLoader('src/templates'),
        autoescape=select_autoescape(['js'])
    )
    template = envjs.get_template('/scripts.js')

    with open('dashboard/scripts.js', 'w') as file:
        file.write(template.render(**kwargs)) 

def main():
    try:
        # Read the fetched data from the csv file and create the dashboard site.
        with open('fetched_data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                create_site(
                    current_power=row['current_power'],
                    current_power_unit=row['current_power_unit'],
                    today_power=row['today_power'],
                    today_power_unit=row['today_power_unit'],
                    month_power=row['month_power'],
                    month_power_unit=row['month_power_unit'],
                    year_power=row['year_power'],
                    year_power_unit=row['year_power_unit'],
                    total_power=row['total_power'],
                    total_power_unit=row['total_power_unit'],
                    co2=row['co2'],
                    co2_unit=row['co2_unit'],
                    coal=row['coal'],
                    coal_unit=row['coal_unit'],
                    tree=row['tree'],
                    last_refresh=row['time'],
                    max_power=st.MAX_POWER,
                    day_goal=st.DAY_GOAL,
                    month_goal=st.MONTH_GOAL
                )
    except Exception as e:
        print(e)
