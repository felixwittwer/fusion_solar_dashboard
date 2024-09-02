[![Static Badge](https://img.shields.io/badge/build for-Gymnasium_Dresden--Plauen-GDP?color=055d3d)](https://gdp.schule/)

# fusion_solar_dashboard
a webscraper that collects data from a fusion solar kiosk website and creates a custom dashboard with it.

## Contact
Felix Wittwer  
**@felixwittwer** on GitHub

[felix.wittwer.mail@gmail.com](mailto:felix.wittwer.mail@gmail.com)


### Drivers

Download the driver matching your version of the installed browser. The Project currently supports **Firefox** with geckodriver and **Chrome** with chromedriver. 

*Be aware that the browser you wana use needs to be installed.*

**Firefox (geckodriver)**

https://github.com/mozilla/geckodriver/releases

Unzip the Folder and put the **geckodriver.exe** file into the main directory of this project.

> tested with v0.34.0 on Windows <br>
> Firefox 126.0 

**Chrome (chromedriver)**

https://googlechromelabs.github.io/chrome-for-testing/#stable

Unzip the Folder and put the **chromedriver.exe** file into the main directory of this project.

> tested with 128.0.6613.86 (r1331488) on Windows <br>
> Chrome version 128.0.6613.86

### Set environment variables

(customize template.env to your needs)

``` cmd
set #to show all current environment variables

set SELENIUM_URL https://****
```

### Configure settings.py

Configure the settings.py file to your needs.
- set your browser
- choose headles or non headless mode
- set browser window height and width
- set the maximum power your solar plant can provide
- set your goal for the day power generation
- set your goal for the month power generation

### Install Python libraries

``` shell
pip install -r requirements.txt
```

<div id="auto_run_py">

## Configure automaticaly running the solar_data_dashboard.py file

### Linux

Set up a crown job.

[I have not tested it on Linux up until now so I dont provide any detailed guide on how to set it up right now.]

### Windows

Start Windows Task Scheduler. (GER: Aufgabenplanung)

Click on "create new Task". (GER: Aufgabe erstellen...)

Give your Task a name and description.

Go to the **Actions** tab. (GER: Aktionen)

Click **new** and put the full path to the python program into the first field. e.g. C:\Users\someone\path_to_script\fusion_solar_dashboard\solar_data_dashboard.py

Put the path to the folder where the whole project lies into the "start in" (GER: Sarten in (optional):) field. e.g. C:\Users\someone\path_to_script\fusion_solar_dashboard\

Click on **OK**.

Go to the **Trigger** tab. (GER: Trigger)

Click **new** and choose **once**. (GER: Einmal)

Tick the first two boxes unter the advanced settings (GER: Erweiterte Einstellungen) section and select your desired intervall times.

</div>

## Actually runnig the program

Note: The finished dashboard can be found in the ***/dashboard/*** folder along with a **JS** and **CSS** file which are mandatory for the dashboard to work!

When the html site is open it automaticaly reloads the html file every 60 seconds.

Make sure that you also run the Python file regularely to update the data that is displayed.

Have a look here if you have not configured it yet. [automatically running solar_data_dashboard.py](#auto_run_py)


## Usefull information

In **routines.py** you can change the order of the individual components. <br>
Additional scripts should be put in the ***/src/parts*** directory. You can add these scripts then to the routines file.
