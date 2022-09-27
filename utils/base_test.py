import os
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



class BaseTest(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def test_home_page(self):
        self.driver.get('https://www.bloomberg.com')



    def tearDown(self):
        self.driver.quit()