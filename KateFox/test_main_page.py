import time
from selenium.webdriver.common.by import By
import pytest

from KateFox.pages_selen.downloads_page import DownloadsPage
from pages_selen.main_page import MainPage
from selenium import webdriver


url = 'https://www.selenium.dev/downloads/'


@pytest.mark.main

class TestMainPageClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        # self.main_page = MainPage(browser, url)
        # self.main_page.open_page()
        self.downloads_page = DownloadsPage(browser, url)
        self.downloads_page.open_page()

    def test_download_latest_verion(self, browser):
        # self.downloads_page.go_to_documentation_page()
        time.sleep(3)
        self.downloads_page.element_is_present(By.CLASS_NAME, '.lead.mt-2.text-left')

