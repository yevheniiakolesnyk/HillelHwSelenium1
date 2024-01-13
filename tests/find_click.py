import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_clicking_menu_items(incognito_hw):
    wait = WebDriverWait(incognito_hw, 10)
    menu_item_1 = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Home')))
    menu_item_1.click()
    time.sleep(1)
    menu_item_2 = incognito_hw.find_element(By.LINK_TEXT, 'News')
    menu_item_2.click()
    time.sleep(1)
    menu_item_3 = incognito_hw.find_element(By.LINK_TEXT, 'Contact')
    menu_item_3.click()
    time.sleep(1)
    menu_item_4 = incognito_hw.find_element(By.LINK_TEXT, 'About')
    menu_item_4.click()
    time.sleep(1)


def test_right_page(headless_hw):
    content = headless_hw.find_element(By.XPATH, '//*[@id="content"]/div/h3')
    text = content.text
    assert text == 'Floating Menu'
