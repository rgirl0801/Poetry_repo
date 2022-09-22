from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.google.ru/")


def test_search_poetry():
    browser.find_element(By.CLASS_NAME, 'gLFyf').send_keys('poetry')
    browser.find_element(By.CLASS_NAME, 'gLFyf').send_keys(Keys.ENTER)
    browser.quit()