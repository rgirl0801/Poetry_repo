import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # browser = webdriver.Chrome(executable_path=r"/Users/kate/WebDriver/chromedriver")
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def url():
    url = 'https://www.selenium.dev/'
    if not url:
        raise Exception("Wrong environment")
    return url
