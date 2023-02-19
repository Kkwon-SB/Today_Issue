from datetime import datetime
from airflow import DAG
from bs4 import BeautifulSoup
import requests
import re
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

default_args = {
    'start_date' : datetime(2023, 2, 2),
}

def _test():
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
        return get_text_title
        
    titles = cleanText(get_text_titles).split()
    word_counts = {}

    for word in titles:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
        
    word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(word_counts[:10])

with DAG(dag_id='daily_hot_topic',
        schedule_interval='*/30 * * * *',
        default_args=default_args,
        tags=['Daily','hot topic','news title crawling'],
        catchup=False
)as dag:
    
    t1 = PythonOperator(
    task_id="crawling_news_title",
    python_callable=_test # 실행할 파이썬 함수
    )

    t2 = PythonOperator(
    task_id="preprocessing",
    python_callable=_test # 실행할 파이썬 함수
    )

    t3 = PythonOperator(
    task_id="word_count",
    python_callable=_test # 실행할 파이썬 함수
    )

    # t4 = PythonOperator(
    # task_id="store_mysql",
    # python_callable=_test # 실행할 파이썬 함수
    # )
    t1 >> t2 >> t3
    
    
    
    
    
    '''
    import csv 
  
  
# field names  
fields = ['Name', 'Branch', 'Year', 'CGPA']  
    
# data rows of csv file  
rows = [ ['Nikhil', 'COE', '2', '9.0'],  
         ['Sanchit', 'COE', '2', '9.1'],  
         ['Aditya', 'IT', '2', '9.3'],  
         ['Sagar', 'SE', '1', '9.5'],  
         ['Prateek', 'MCE', '3', '7.8'],  
         ['Sahil', 'EP', '2', '9.1']]  
  
with open('test.csv', 'w',newline='') as f: 
      
    # using csv.writer method from CSV package 
    write = csv.writer(f) 
      
    write.writerow(fields) 
    write.writerows(rows)
[출처] 파이썬 list를 csv로 저장|작성자 용용
    '''