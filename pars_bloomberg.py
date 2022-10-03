"""Найти сколько раз слово money встречается в новостях"""
import re
import string
import uuid
import os
import requests
import json
import random
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


class CountMoney:

    def get_html(self, url):
        headers = {
            "User-Agent": "PostmanRuntime/7.29.2",
            "Postman-Token": str(uuid.uuid4()),
        }
        response = requests.get(url, headers=headers)
        return response.text

    def get_list_link_news(self, array):
        data_now = datetime.now()
        today_day = data_now.strftime("%B %d")
        date_ = " ".join([day if len(day) <= 2 else day[:3] for day in today_day.split()])
        lst_url = list(map(lambda x: x['url'] if date_ in x['publishedAt'] else None, json.loads(array)))
        return lst_url

    def get_text_news(self, driver, url):
        html = self.get_html(url)
        with open('news.html', 'w', encoding='utf-8') as file:
            file.write(html)
        driver.get("file://" + os.path.join(os.getcwd(), 'news.html'))
        try:
            category = driver.find_element(By.CSS_SELECTOR, "span.brand__3ac459ef").text
        except:
            category = " "
        try:
            title = driver.find_element(By.CSS_SELECTOR, 'h1').text
        except:
            title = " "
        try:
            text_new = driver.find_element(By.CSS_SELECTOR, 'div.body-content').text
        except:
            text_new = " "
        result_new = category + " " + title + " " + text_new
        return re.sub(r"\s+", " ", result_new.strip(string.punctuation)).lower().split()


if __name__ == '__main__':
    word = input("Введите слово для подсчета числа повторения в новостях: ").lower()
    lst_words_from_news = []
    cm = CountMoney()
    meta_datas = cm.get_html(
        "https://personalization.bloomberg.com/user/recommendations/meta?countryCode=RU&country=RU&field_d=ertelecom.ru&field_n=hf&trackingRegion=Europe&cacheExpiredTime=1664818510463&region=Europe&fieldN=hf&fieldD=ertelecom.ru&session_id=8064046e-26e8-4f95-b249-dff1cf5901f8&session_key=efb9a7a20f0c62abe13efbbb1e536fc8228b3ba3&agent_id=d092c874-e44b-45fd-8eb8-a00dbde25a4f&timezoneOffset=-10800000&exp_pref=EUR&application=javelin&exclude=Story%7CRIXPS6DWX2PT01%3BStory%7CRIXH09T0G1KY01%3BStory%7CRIYB0CDWRGG301%3BStory%7CRIY767TVI5MO02%3BStory%7CRIXRKCT1UM0Y01%3BStory%7CRIXO24DWRGG001%3BStory%7CRITFZCDWX2Q501%3BStory%7CRIWJ5ZT0G1KW01%3BStory%7CRIYOWEDWLU6C01%3BStory%7CRIYKJXDWX2PS01%3BStory%7CRIYDU3DWLU6801%3BStory%7CRIM9K9T1UM0W01%3BStory%7CRIW8V1DWX2PS01%3BStory%7CRIW58CDWX2PT01%3BStory%7CRIVQNGDWLU6801%3BStory%7CRIVGD2DWX2PS01%3BStory%7CRIYROHT1UM1601%3BStory%7CRIY0V1DWRGG001%3BStory%7CRIXXBQDWLU6C01%3BStory%7CRIXPTRDWX2PS01%3BInteractive%7CRIYROFDWRGG001%3BStory%7CRIYJLZT0AFB501%3BStory%7CRIXXS4T0AFB601%3BStory%7CRIXRHVDWLU6801%3BVideo%7CRIVTGOT0G1KW01%3BVideo%7CRIX6ISDWLU6B01%3BVideo%7CRITXETT0AFB401%3BVideo%7CRITZEZT1UM1201%3BStory%7CRIXZYMTP3SHX%3BStory%7CRIVU1ADWRGG201%3BStory%7CRIXO7KT1UM0W01%3BStory%7CRIX2A8DWRGG401%3BStory%7CRIXR18DWX2PV01%3BStory%7CRIXNSUT0AFB401%3BStory%7CRIX5CDDWX2PW01%3BStory%7CRIWQ34T0AFB401%3BStory%7CRIYHMZDWLU6801%3BStory%7CRIXBPGDWRGG501%3BStory%7CRIYKONT0G1L801%3BStory%7CRIYDSKT0G1L101%3BStory%7CRIYDSJT0G1L001%3BStory%7CR9IPK1T0AFB701%3BStory%7CR18T6YDWLU6D01%3BStory%7CQRTGZDT0G1L501%3BStory%7CQL2W4BT1UM1701%3BStory%7CQGO86WT0G1L001%3BStory%7CQBNSHXT0AFBA01%3BStory%7CRIYH4CDWLU6801%3BStory%7CRIYJZQDWLU6A01%3BStory%7CRIYHJYDWX2PS01%3BStory%7CRIX0AIDWX2PU01%3BInteractive%7CRITENET1UM0X01%3BStory%7CRHXNM2T1UM1201%3BStory%7CRIWJ4KDWX2PU01%3BStory%7CRIXZWEDWRGG201%3BStory%7CRIYLHTDWX2PS01%3BStory%7CRIYLH8DWRGG501%3BStory%7CRIYGT0DWLU6801%3BStory%7CRIXD70DWX2PS01%3BStory%7CRIYQDODWX2PS01%3BStory%7CRIYRDQDWRGG101%3BStory%7CRIYRYYDWRGG001%3BStory%7CRI56SODWX2PU01%3BStory%7CRIYDJADWRGG001%3BStory%7CRIXVYSDWX2PS01%3BStory%7CRIYDBNDWRGG001%3BStory%7CRIYDSHT0AFB501%3BStory%7CRIXSCZDWRGG001%3BStory%7CRIXCMWDWLU6B01%3BStory%7CRIVK0MDWLU6901%3BStory%7CRIWPAVDWLU6801%3BStory%7CRIV58DDWLU6901%3BStory%7CRIX8NJDWX2PU01%3BStory%7CRIT7IJDWX2PT01%3BStory%7CRIYK0CDWRGG601%3BStory%7CRIYDSGDWRGG001%3BFeature%7CRIXMYFT0AFB401%3BStory%7CRIX77HDWX2PS01%3BStory%7CRIUWGRDWRGG001%3BStory%7CRIWRVBDWRGGO01%3BStory%7CRIWPWLDWLU6901%3BStory%7CRIWODFDWX2PU01%3BStory%7CRIYHYBT1UM0W01%3BStory%7CRIYDSBT1UM1001%3BStory%7CRIYDSFDWLU6801%3BStory%7CRIYDSKT0AFBB01&limit=143&algorithm=meta&resourceTypes=Story%3BFeature%3BInteractive%3BQuicktake&inactivePeriod=2592000000&interactionsLimit=1&maxAge=604800000&filters.exclude.Ni=FIVEEU%3BEURFIVE%3BAPACFIVE%3BAPACEVE%3BEUREVE%3BFIVE%3BUSEVE%3BGLOBWRP%3BUPDATE&thumbnailRequired=true&rescorers=random%3Btpx%3BsimilarResources&decayCoefficient=1&maxAge.ni.USSTOCKS=43200000&rescorers.random.minimumScore=0.1&rescorers.similarResources.minimumScore=0.01&rescorers.similarResources.groupSimilarResources=false")
    lst_news_link = cm.get_list_link_news(meta_datas)
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-application-cache')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-dev-shm-usage")
    options.headless = True
    with webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options) as driver:
        i = 0
        for index, link in enumerate(lst_news_link):
            if link is not None:
                print(f"Обрабатывается {i} новость")
                if link is not None and index % 5 == 0 and index != 0:
                    sleep(random.uniform(40, 60))
                words = cm.get_text_news(driver, link)
                lst_words_from_news.extend(words)
                sleep(random.uniform(3.7, 8.9))
                i += 1
        print(f"Искомое слово в новостях за сутки встретилось  {lst_words_from_news.count(word)} раз")
