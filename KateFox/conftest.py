import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    browser.quit()
