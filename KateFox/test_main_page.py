import time

import pytest

from KateFox.pages.main_page import MainPage


url = 'https://www.selenium.dev/'


@pytest.mark.main
class TestMainPageClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser, url)
        self.main_page.open_page()

    def test_header_text_is_present(self):
        assert self.main_page.text_is_present() == "Selenium automates browsers. That's it!"
        # TODO: google text assert

    def test_go_to_webdriver(self, browser):
        self.main_page.go_to_webdriver()

    def test_go_to_ide(self, browser):
        self.main_page.go_to_ide()

    def test_go_to_grid(self, browser):
        self.main_page.go_to_grid()
        time.sleep(5)

