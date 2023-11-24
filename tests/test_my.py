from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com.ua')
search = driver.find_element(By.ID,'APjFqb')
search.send_keys('Selenium')
# btn = driver.find_element(By.CLASS_NAME, 'gN089b')
# btn.click()
input()

url = driver.current_url
print(url)