from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path=r"/Users/kate/WebDriver/chromedriver")
browser.get('https://www.selenium.dev/')
#
# browser.find_element(By.CLASS_NAME, '.lead.mt-2').click()
#
#
# browser.find_element(By.XPATH,
#                          "//*[contains(text(),'4.5.0')]").click()
# time.sleep(2)
# browser.find_element(By.XPATH,
#                          "//a[@href ='https://selenium.dev/documentation/en/grid/']").click()


r = browser.find_element(By.CSS_SELECTOR, '.display-1.mt-0').text
print(r)

time.sleep(5)


browser.quit()
