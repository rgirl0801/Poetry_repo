from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    WELCOME_TXT = (By.CLASS_NAME, '.display - 1.mt - 0')


    def welcome_text_is_present(self):
        assert self.element_is_present(self.WELCOME_TXT)
