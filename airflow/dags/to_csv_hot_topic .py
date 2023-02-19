from datetime import datetime
from airflow import DAG
from bs4 import BeautifulSoup
import requests
import re
import csv
from airflow.operators.python import PythonOperator

default_args = {
    'start_date' : datetime(2023, 2, 2),
}


def crawling(**context):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    inputURL = "https://news.naver.com/main/ranking/popularMemo.naver" #댓글 많은 뉴스 순으로, 목적에 취합, 핫토픽이기 때문에
    response = requests.get(inputURL, headers=headers)
    beautifulSoup = BeautifulSoup(response.content, "html.parser")
    titles = beautifulSoup.find_all("a", attrs={"class":"list_title nclicks('RBP.cmtnws')"})
    get_text_titles =""

    for title in titles:
        get_text_titles += (title.get_text())

    context['task_instance'].xcom_push(key='pushed_crawling_value', value=get_text_titles)
    
    
def processing_count(**context):
    crawled_date = context['task_instance'].xcom_pull(key='pushed_crawling_value', task_ids='crawling_news_title')
    print('crawled_date',crawled_date)
    re_date = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'\“\”\‘\’\·…》]',' ', crawled_date).split()
    print('re_date',re_date)
    word_counts = {}

    for word in re_date:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
        
    word_counts2 = sorted(word_counts,key=lambda x:word_counts[x], reverse=True)[:10]
    # print('word_counts2',word_counts2)
    
    num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = [i for i in word_counts2]
    context['task_instance'].xcom_push(key='processed_count_value', value=word_counts2)
    print(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)

def store_to_csv(**context):
    processed_count_value = context['task_instance'].xcom_pull(key='processed_count_value', task_ids='processing_count')
    with open('test.csv', 'a',newline='', encoding='UTF-8') as f:  #w 새롭게, a이어서
            write = csv.writer(f)
            write.writerow(processed_count_value)

    # print(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)

with DAG(dag_id='to_csv1',
        schedule_interval='*/30 * * * *',
        default_args=default_args,
        tags=['Daily','hot topic','news title crawling'],
        catchup=False
)as dag:
    
    t1 = PythonOperator(
    task_id="crawling_news_title",
    python_callable=crawling
    )
    t2 = PythonOperator(
    task_id="processing_count",
    python_callable=processing_count 
    )
    t3 = PythonOperator(
    task_id="store_to_csv",
    python_callable=store_to_csv 
    )

    t1 >> t2 >> t3