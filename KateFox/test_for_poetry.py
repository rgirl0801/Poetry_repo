import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_count_money():
    browser.get("https://www.bloomberg.com/")
    assert browser.title == "Bloomberg.com", "Invalid title"
    browser.find_element(By.CLASS_NAME, "single-story-module__headline-link").send_keys(
        Keys.COMMAND, "F"
    )
    time.sleep(5)
    browser.quit()
