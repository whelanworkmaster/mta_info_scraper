import time
from selenium import webdriver


def scrape_selenium(url, driver):
    driver.get(url)
    statuses = driver.find_element_by_id('tab-subway')

    print(statuses.text)

    time.sleep(5.0)


if __name__ == '__main__':
    info_url = 'https://new.mta.info/'

    web_driver = webdriver.Firefox()
    while True:
        scrape_selenium(info_url, web_driver)
