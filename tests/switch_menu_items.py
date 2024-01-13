import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://magento.softwaretestingboard.com/"

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    yield driver
    time.sleep(2)
    driver.quit()


def test_do(driver):
    wait = WebDriverWait(driver,10)
    top_menu_item_1 = wait.until(EC.element_to_be_clickable((By.ID, 'ui-id-3')))
    top_menu_item_1.click()
    time.sleep(2)
    top_menu_item_2 = driver.find_element(By.ID, 'ui-id-4')
    top_menu_item_2.click()
    time.sleep(2)
    top_menu_item_3 = driver.find_element(By.ID, 'ui-id-5')
    top_menu_item_3.click()
