from selenium import webdriver
import os
import time
import pandas as pd
import re

loc = os.path.abspath(os.getcwd()) + "\\chromedriver.exe"
driver = webdriver.Chrome(loc)
driver.get("https://www.instagram.com")
time.sleep(10)
userNameId='//*[@id="loginForm"]/div/div[1]/div/label/input'
userName="XXXXXXXX"
password="XXXXXXXX"
passwordId='//*[@id="loginForm"]/div/div[2]/div/label/input'
loginId='//*[@id="loginForm"]/div/div[3]/button/div'
driver.find_element_by_xpath(userNameId).click()
driver.find_element_by_xpath(userNameId).send_keys(userName)
driver.find_element_by_xpath(passwordId).click()
driver.find_element_by_xpath(passwordId).send_keys(password)
driver.find_element_by_xpath(loginId).click()
time.sleep(5)
saveInfoId='//*[@id="react-root"]/section/main/div/div/div/section/div/button'
driver.find_element_by_xpath(saveInfoId).click()
time.sleep(5)
turnNotificationId='/html/body/div[4]/div/div/div/div[3]/button[2]'
# driver.find_element_by_xpath(turnNotificationId).click()
likes_tag = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button/span'
username_tag = '//*[@id="react-root"]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a'
links_df = pd.read_excel("reelsLink.xlsx")
output_df = pd.DataFrame(columns=['url','username','likes','comment'])
for link in links_df['Link']:
    try:
        print("Getting data for : {}".format(link))
        row = dict()
        row['url'] = link
        driver.switch_to.window(driver.window_handles[-1])
        driver.execute_script('''window.open("{}","_blank");'''.format(link))
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])
        content = driver.page_source
        comment_list = re.findall("\"edge_media_to_parent_comment\":{\"count\":[0-9,]+",content)
        if len(comment_list) == 1:
            row['comment'] = comment_list[0].split(":")[-1]
        else:
            row['comment'] = 'error'
        driver.switch_to.window(driver.window_handles[-1])
        row['likes'] = driver.find_element_by_xpath(likes_tag).text
        row['username'] = driver.find_element_by_xpath(username_tag).text
        driver.close()
        print(row)
        output_df = output_df.append(row,ignore_index=True)
    except Exception as e:
        print(e)
        row['url'] = link
        row['username'] = 'error'
        row['likes'] = 'error'
        row['comment'] = 'error'
        print(row)
        output_df = output_df.append(row,ignore_index=True)
driver.quit()
print("Saving Data...")
output_df.to_excel("retrieved_reels_views.xlsx",index=False)
print("Done...")
input()
