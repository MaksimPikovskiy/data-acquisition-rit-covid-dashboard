from selenium import webdriver
from bs4 import BeautifulSoup
import pandas


def main():
    url = 'https://www.rit.edu/ready/spring-2022-dashboard'
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get(url)

    casesStudents = []
    casesEmployees = []
    casesStudents.append(0)
    casesEmployees.append(0)
    print(*casesEmployees)

    content = driver.page_source
    soup = BeautifulSoup(content)

    current_cases_students = soup.find_element(webdriver.XPATH,
                                                 '/html/body/div[3]/main/div[2]/div[3]/div[3]/div/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div/p')

    current_cases_employees = soup.find_element(webdriver.XPATH,
                                                  '/html/body/div[3]/main/div[2]/div[3]/div[3]/div/div/div/div[2]/div/div[4]/div/div/div/div/div[2]/div/p')


    casesStudents.append(current_cases_students.text)
    casesEmployees.append(current_cases_employees.text)

    for x in range(len(casesEmployees)):
        print(casesEmployees[x])
