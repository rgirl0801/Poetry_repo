import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser = webdriver.Chrome(executable_path=r"/Users/kate/WebDriver/chromedriver")
    browser.maximize_window()
    yield browser
    browser.quit()

# @pytest.fixture()
# def url():
#     """Фикстура для получения заданного из командной строки окружения"""
#     # env = request.config.getoption("--env")
#     url = 'https://www.selenium.dev/'
#     if not url:
#         raise Exception("Передано неверное окружение")
#     return url
