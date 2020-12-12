from selenium import webdriver
import time
import numpy as np
import os
import threading
import requests
import socket
import sys
from lxml.html import fromstring
from concurrent.futures import ThreadPoolExecutor


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        try:
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
        except Exception as e:
            print("Error while getting proxy : ", e)
    return proxies

def auto(url):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        PROXY = list(get_proxies())
        if(len(PROXY) != 0):
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument('--proxy-server=%s' % PROXY[np.random.randint(0,len(PROXY))])    
        loc = os.path.abspath(os.getcwd()) + "/chromedriver"
        driver = webdriver.Chrome(loc, chrome_options=chrome_options)
        driver.get(url)
        time.sleep(np.random.randint(5,10))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(np.random.randint(5,10))
        case_study_path = '//*[@id="comp-k9y7oef73label"]'
        driver.find_element_by_xpath(case_study_path).click()
        time.sleep(np.random.randint(5,10))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(np.random.randint(5,10))
        print("Successful click : ",i+1)
        print("auto assigned to thread: {}\n\n".format(threading.current_thread().name))
        driver.quit()
    except Exception as e :
        print("ERROR : ",e)
        time.sleep(5)

url = str(sys.argv[1])
with ThreadPoolExecutor(max_workers=20) as executor:
        for _ in range(40):
            future = executor.submit(auto, (url))
            print(future)