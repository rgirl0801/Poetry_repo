from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://www.selenium.dev/downloads')
#
# browser.find_element(By.XPATH,
#     "//a[@href ='https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.5.0/selenium-server-4.5.0.jar']").click()

# browser.find_element(By.XPATH, "xpath=//a[contains(@href,'Selenium')")
browser.find_element(By.XPATH, "//a[contains(@href,'https://github.com/SeleniumHQ/')]").click()


time.sleep(2)

browser.quit()


# from string import printable
#
# print(printable)
