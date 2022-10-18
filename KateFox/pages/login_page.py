from .locators import LoginPageLocators
from .base_page import BasePage
from KateFox.pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, "//form[@id='register_form']//button")

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_FORM)


    def sign_up(self, email: str, password: str) -> None:
        self.wait_until_clickable(self.REG_EMAIL).send_keys(email)
        self.wait_until_clickable(self.REG_PASSWORD).send_keys(password)
        self.wait_until_clickable(self.CONFIRM_PASSWORD).send_keys(password)
        self.wait_until_clickable(self.REG_BTN).click()