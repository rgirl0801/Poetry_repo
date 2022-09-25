import requests
from bs4 import BeautifulSoup


def count_selenium():
    url = 'https://www.selenium.dev/'
    resp = requests.get(url)

    if resp.status_code == 200:
        print("Successfully opened the web page")
        soup = BeautifulSoup(resp.text, 'html.parser')
        all_text = soup.get_text()
        n = all_text.count('Selenium')
        print(f'{n} times the word "Selenium" occurs')
    else:
        print("Error")


count_selenium()
