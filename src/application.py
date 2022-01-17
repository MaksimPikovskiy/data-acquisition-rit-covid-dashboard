from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import csv
import pandas

URL = 'https://www.rit.edu/ready/spring-2022-dashboard'
PATH = 'D:\PyCharm Projects\data-acquisition-rit-covid-dashboard\website_screenshots'
DATA_PATH = 'D:\PyCharm Projects\data-acquisition-rit-covid-dashboard\data'


def save_data(students, employees):
    df = pandas.read_csv(DATA_PATH + '\\' + 'covid_cases.csv')

    data = {
        'Students': [students],
        'Employees': [employees]
    }

    df = pandas.DataFrame(data)

    df.to_csv(DATA_PATH + '\\' + 'covid_cases.csv', mode='a', index=False, header=False)


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


def main() -> None:
    s = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')

    driver = webdriver.Chrome(service=s, options=options)
    driver.get(URL)

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    body = soup.body

    data_students = body.find('div',
                              class_='card statistic statistic-16723 position-relative h-100 text-align-center paragraph paragraph--type--statistic paragraph--view-mode--default')
    data_employees = body.find('div',
                               class_='card statistic statistic-16726 position-relative h-100 text-align-center paragraph paragraph--type--statistic paragraph--view-mode--default')

    current_cases_students = int(data_students.find('p').text)
    current_cases_employees = int(data_employees.find('p').text)

    print(current_cases_students)
    print(current_cases_employees)

    save_screenshot(driver)

    save_data(current_cases_students, current_cases_employees)

    driver.close()
    driver.quit()


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
