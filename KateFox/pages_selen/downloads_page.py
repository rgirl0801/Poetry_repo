from selenium.webdriver.common.by import By

from KateFox.pages_selen.base_page import BasePage


class DownloadsPage(BasePage):
    DOWNLOAD_TXT = (By.CLASS_NAME, '.lead.mt-2.text-left')
    DOWNLOAD_BTN = (By.XPATH,
                    "//a[@href ='https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.5.0/selenium-server-4.5.0.jar']")
    DOCUMENTATION_BTN = (By.XPATH,
                         "//a[@href ='https://selenium.dev/documentation/en/grid/']")


    def download_text_is_present(self):
        assert self.element_is_present(self.DOWNLOAD_TXT)


    # def download_latest_version(self):
    #     self.wait_until_clickable(self.DOWNLOAD_BTN).click()


    def go_to_documentation_page(self):
        self.wait_until_clickable(self.DOCUMENTATION_BTN).click()
