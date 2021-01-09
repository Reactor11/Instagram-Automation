import requests
import re
import pandas as pd
import numpy as np
from selenium import webdriver
import os
import time
links_df = pd.read_excel("reelsLink.xlsx")
output_df = pd.DataFrame(columns=['url','username','views','likes'])
count = 1
for link in links_df['Link']:
    try:
        print("Count : {} out of {}".format(str(count),str(len(links_df))))
        count+=1
        print("Getting data for : {}".format(link))
        row = dict()
        row['url'] = link
        user_agent = {'User-agent': 'Mozilla/5.0'}
        content = requests.get(link,headers=user_agent).content.decode("utf-8")
        views_list = re.findall("\"video_play_count\":[0-9]+",content)
        if len(views_list) == 1:
            row['views'] = views_list[0].split(":")[-1]
        else:
            row['views'] = 'error'
        likes_list = re.findall("\"edge_media_preview_like\":{\"count\":[0-9]+",content)
        if len(likes_list) == 1:
            row['likes'] = likes_list[0].split(":")[-1]
        else:
            row['likes'] = 'error'
        username_list = re.findall("\"alternateName\":\".+?\"",content)
        if len(username_list) >= 1:
            row['username'] = username_list[0].split(":")[-1]
        else:
            row['username'] = 'error'
        print(row)
        output_df = output_df.append(row,ignore_index=True)
    except Exception as e:
        print(e)
        row['url'] = link
        row['username'] = 'error'
        row['views'] = 'error'
        row['likes'] = 'error'
        output_df = output_df.append(row,ignore_index=True)
print("Saving Data...")
output_df.to_excel("retrieved_reels_views.xlsx",index=False)
print("Done...")
input()
