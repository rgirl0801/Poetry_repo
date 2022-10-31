from selenium.webdriver.common.by import By

from KateFox.pages.base_page import BasePage


class MainPage(BasePage):
    WELCOME_TXT = (By.CSS_SELECTOR, '.display-1.mt-0')
    WEBRDIVER_BTN = (By.CSS_SELECTOR, '.selenium-button.selenium-webdriver')
    IDE_BTN = (By.CSS_SELECTOR, '.selenium-button.selenium-ide')
    GRID_BTN = (By.CSS_SELECTOR, '.selenium-button.selenium-grid')


    def text_is_present(self):
        assert "Selenium automates browsers. That's it!" in self.wait_until_visible(
            self.WELCOME_TXT).text, \
            "Text has not been displayed"


    def go_to_webdriver(self):
        self.wait_until_clickable(self.WEBRDIVER_BTN).click()

    def go_to_ide(self):
        self.wait_until_clickable(self.IDE_BTN).click()

    def go_to_grid(self):
        self.wait_until_clickable(self.GRID_BTN).click()
