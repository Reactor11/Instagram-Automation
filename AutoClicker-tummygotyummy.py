from selenium import webdriver
import time
import numpy as np
import os
import threading
import requests
import socket
import sys
from lxml.html import fromstring

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]') and i.xpath('.//td[3][contains(text(),"IN")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def auto(rep,url):
    for i in range(rep):
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
            print("Successful click : ",i+1)
            print("auto assigned to thread: {}\n\n".format(threading.current_thread().name))
            driver.quit()
        except Exception as e :
            print("ERROR : ",e)
            time.sleep(5)

url = str(sys.argv[1])
rep = 500

for i in range(rep):
  





print("All done!")
