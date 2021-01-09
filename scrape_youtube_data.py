import requests
import re
import pandas as pd
import numpy as np
from selenium import webdriver
import os
import time
links_df = pd.read_excel("reelsLink.xlsx")
output_df = pd.DataFrame()
for link in links_df['Link']:
    try:
        print("Getting data for : {}".format(link))
        row = dict()
        row['url'] = link
        user_agent = {'User-agent': 'Mozilla/5.0'}
        content = requests.get(link,headers=user_agent).content.decode("utf-8")
        likes_list = re.findall('\"likeStatus\":\"INDIFFERENT\",\"tooltip\":\"[0-9,]+',content)
        if len(likes_list) == 1:
            row['likes'] = likes_list[0].split("\"")[-1]
        else:
            row['likes'] = 'error'
        views_list = re.findall('\"viewCount\":{\"simpleText\":\"[0-9,]+',content)
        if len(views_list) == 1:
            row['views'] = views_list[0].split("\"")[-1]
        else:
            row['views'] = 'error'
        names_list = re.findall('\"ownerChannelName\":\"[A-Za-z0-9\s]+',content)
        if len(names_list) == 1:
            row['Channel Name'] = names_list[0].split("\"")[-1]
        else:
            row['Channel Name'] = 'error'
        date_list = re.findall('\"publishDate\":\"[0-9-]+',content)
        if len(date_list) == 1:
            row['date'] = date_list[0].split("\"")[-1]
        else:
            row['date'] = 'error'
        #time.sleep(5)
        print(row)
        output_df = output_df.append(row,ignore_index=True)
    except Exception as e:
        print(e)
        row['url'] = link
        row['likes'] = 'error'
        row['views'] = 'error'
        row['Channel Name'] = 'error'
        row['date'] = 'error'
        output_df = output_df.append(row,ignore_index=True)
print("Saving Data...")
output_df.to_excel("retrieved_reels_views.xlsx",index=False)
print("Done...")
input()
