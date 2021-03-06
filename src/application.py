# Script that retrieves Positive COVID Cases from RIT COVID Dashboard: https://www.rit.edu/ready/spring-2022-dashboard
# Made by Maksim Pikovskiy
# pikmak2001@gmail.com

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas
import numpy
import matplotlib.pyplot as plt
import time
import sender

__author__ = "Maksim Pikovskiy"
__email__ = "pikmak2001@gmail.com"
__version__ = "2.0.0"
__copyright__ = "Copyright 2022"
__status__ = "Production"

# General Variable for the Program
URL = 'https://www.rit.edu/ready/spring-2022-dashboard'
PATH = 'website_screenshots'
DATA_PATH = 'data'


# Creates graphs using generated CSV file
def create_graph():
    df = pandas.read_csv(DATA_PATH + '\\' + 'covid_cases.csv')

    x_axis = range(1, df['Students'].size + 1)

    plt.plot(x_axis, df['Students'], 'b', label='Students')
    sizeStudents = df['Students'].size
    i = 0
    for x, y in zip(x_axis, df['Students']):
        if i == sizeStudents - 1 or i == sizeStudents - 2:
            plt.annotate(y,
                         (x, y),
                         textcoords="offset points",
                         xytext=(0, 10),
                         ha='center')
        i += 1

    plt.plot(x_axis, df['Employees'], 'r', label='Employees')
    sizeEmployees = df['Employees'].size
    i = 0
    for x, y in zip(x_axis, df['Employees']):
        if i == sizeEmployees - 1 or i == sizeEmployees - 2:
            plt.annotate(y,
                         (x, y),
                         textcoords="offset points",
                         xytext=(0, 10),
                         ha='center')
        i += 1

    plt.plot(x_axis, df['Total'], 'g', label='Total')
    sizeTotal = df['Total'].size
    i = 0
    for x, y in zip(x_axis, df['Total']):
        if i == sizeTotal - 1 or i == sizeTotal - 2:
            plt.annotate(y,
                         (x, y),
                         textcoords="offset points",
                         xytext=(0, 10),
                         ha='center')
        i += 1

    future_x_axis = range(1, len(x_axis) + 5)

    z = numpy.polyfit(x_axis, df['Students'], 1)
    p = numpy.poly1d(z)
    plt.plot(future_x_axis, p(future_x_axis), 'b--')

    z = numpy.polyfit(x_axis, df['Employees'], 1)
    p = numpy.poly1d(z)
    plt.plot(future_x_axis, p(future_x_axis), 'r--')

    z = numpy.polyfit(x_axis, df['Total'], 1)
    p = numpy.poly1d(z)
    plt.plot(future_x_axis, p(future_x_axis), 'g--')

    plt.title('Positive Covid Cases Over Spring Semester')
    plt.xlabel('Days (since January 10th)')
    plt.ylabel('Positive Covid Cases')
    plt.grid(True)
    plt.xticks(numpy.arange(min(future_x_axis) + 1, max(future_x_axis) + 1, 2.0))
    plt.legend()
    plt.savefig(DATA_PATH + '\\' + 'covid_cases_graph.png', dpi=900)


# Appends data to existing CSV file
def save_data(students, employees):
    data = {
        'Students': [students],
        'Employees': [employees],
        'Total': [(students + employees)]
    }

    df = pandas.DataFrame(data)

    df.to_csv(DATA_PATH + '\\' + 'covid_cases.csv', mode='a', index=False, header=False)


# Saves screenshot of data on RIT COVID Dashboard
def save_screenshot(driver):
    total_files = 0
    for base, dirs, files in os.walk(PATH):
        for Files in files:
            total_files += 1

    driver.maximize_window()
    scheight = .1
    while scheight < 5.4:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight/%s);' % scheight)
        scheight += .01
    driver.save_screenshot(PATH + '\\' + 'screenshot' + (str(total_files + 1)) + '.png')


# Main body of the program, which initiates the web driver and gets the data from the RIT COVID Dashboard.
# Calls on other methods to generate data.
def main() -> None:
    print(__author__)
    print(__email__)
    print(__version__)
    print(__copyright__)
    print(__status__)

    s = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--log-level=1')

    driver = webdriver.Chrome(service=s, options=options)
    driver.get(URL)

    time.sleep(65)

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    body = soup.body

    data_students = body.find('div',
                              class_='card statistic statistic-16723 position-relative h-100 text-align-center paragraph paragraph--type--statistic paragraph--view-mode--default')
    data_employees = body.find('div',
                               class_='card statistic statistic-16726 position-relative h-100 text-align-center paragraph paragraph--type--statistic paragraph--view-mode--default')

    current_cases_students = int(data_students.find('p').text)
    current_cases_employees = int(data_employees.find('p').text)

    save_screenshot(driver)

    save_data(current_cases_students, current_cases_employees)

    create_graph()

    driver.close()
    driver.quit()


# only run this program if it is not being imported by another main module
# runs senders script to send the generated graph
if __name__ == '__main__':
    main()
    sender.main()
