import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
inputURL = "https://news.naver.com/main/ranking/popularMemo.naver" #댓글 많은 뉴스 순으로, 목적에 취합, 핫토픽이기 때문에
response = requests.get(inputURL, headers=headers)
beautifulSoup = BeautifulSoup(response.content, "html.parser")
titles = beautifulSoup.find_all("a", attrs={"class":"list_title nclicks('RBP.cmtnws')"})
get_text_titles =""

for title in titles:
    get_text_titles += (title.get_text())
    
def cleanText(get_text_titles):
    get_text_title = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'\“\”\‘\’\·…》]',' ', get_text_titles)
    print(get_text_title)
    return get_text_title
    
titles = cleanText(get_text_titles).split()
word_counts = {}

for word in titles:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
    
word_counts = sorted(word_counts,key=lambda x:word_counts[x], reverse=True)[:10]


# fields = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',] 

with open('test.csv', 'a',newline='', encoding='UTF-8') as f:  #w 새롭게, a이어서
        write = csv.writer(f)
        write.writerow(word_counts)
        