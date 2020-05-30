from selenium import webdriver
import time
import numpy as np
import os
import threading
import requests
import socket
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

url = "https://www.socialmatte.com"
rep = 20//10

t1 = threading.Thread(target=auto, name='t1',args=(rep,url,))
t2 = threading.Thread(target=auto, name='t2',args=(rep,url,))
t3 = threading.Thread(target=auto, name='t3',args=(rep,url,))
t4 = threading.Thread(target=auto, name='t4',args=(rep,url,))
t5 = threading.Thread(target=auto, name='t5',args=(rep,url,))
t6 = threading.Thread(target=auto, name='t6',args=(rep,url,))
t7 = threading.Thread(target=auto, name='t7',args=(rep,url,))
t8 = threading.Thread(target=auto, name='t8',args=(rep,url,))
t9 = threading.Thread(target=auto, name='t9',args=(rep,url,))
t10 = threading.Thread(target=auto, name='t10',args=(rep,url,))


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

print("All done!")
