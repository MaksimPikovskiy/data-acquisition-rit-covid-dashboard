from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas


def main() -> None:
    s = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')

    url = 'https://www.rit.edu/ready/spring-2022-dashboard'
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(url)

    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")
    body = soup.body

    data_students = body.find("div", class_="card statistic statistic-16723 position-relative h-100 text-align-center paragraph paragraph--type--statistic paragraph--view-mode--default")
    data_employees = body.find("div", class_="card statistic statistic-16726 position-relative h-100 text-align-center paragraph paragraph--type--statistic paragraph--view-mode--default")

    current_cases_students = int(data_students.find('p').text)
    current_cases_employees = int(data_employees.find('p').text)

    print(current_cases_students)
    print(current_cases_employees)

    driver.close()
    driver.quit()


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
