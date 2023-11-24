import time

import pytest
from selenium import webdriver


@pytest.fixture()
def incognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.google.com')
    return driver


@pytest.fixture()
def headless():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.google.com')
    return driver


@pytest.fixture()
def incognito_hw():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://the-internet.herokuapp.com/floating_menu#home')
    driver.implicitly_wait(30)
    yield driver
    time.sleep(3)
    driver.quit()


@pytest.fixture()
def headless_hw():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://the-internet.herokuapp.com/floating_menu#home')
    yield driver
    driver.quit()
