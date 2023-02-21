#csv db통합

from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow import DAG
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import csv
import re

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
    
    
def Pre_processing(**context):
    crawled_date = context['task_instance'].xcom_pull(key='pushed_crawling_value', task_ids='crawling_data')
    processed_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'\“\”\‘\’\·…》]',' ', crawled_date).split()
    
    word_counts = {}

    for word in processed_data:
        if len(word) <= 1:
            continue
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
        
    word_counts2 = sorted(word_counts,key=lambda x:word_counts[x], reverse=True)[:10]

    context['task_instance'].xcom_push(key='processed_count_value', value=word_counts2)



def save_to_csv(**context):
    from datetime import datetime ###
    
    word_counted = context['task_instance'].xcom_pull(key='processed_count_value', task_ids='Pre_processing')
    word_counted.append(datetime.now())
    try:
        f = open('csv_mysql.csv', 'r')
        with open('csv_mysql.csv', 'a',newline='', encoding='UTF-8') as f: 
                write = csv.writer(f)  
                write.writerow(word_counted)
    except:
        #처음 작업
        fields = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','Data_Time']
        with open('csv_mysql.csv', 'w',newline='', encoding='UTF-8') as f: 
                write = csv.writer(f) 
                write.writerow(fields) 
                write.writerow(word_counted)
    
    
def save_to_mysql(**context):
    from datetime import datetime ###
    import pymysql
    
    word_counted = context['task_instance'].xcom_pull(key='processed_count_value', task_ids='Pre_processing')
    word_counted.append(datetime.now())
    
    conn = pymysql.connect(
    host='192.168.0.214', 
    user="airflow_kwon",
    database= "mydatabase",
    password= "q1w2e3r4",
    charset='utf8')

    sql = "INSERT INTO sql_test000 (1st, 2nd, 3rd, 4th, 5th, 6th, 7th ,8th ,9th, 10th) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (word_counted[0],word_counted[1],word_counted[2],word_counted[3],word_counted[4],word_counted[5],word_counted[6],word_counted[7],word_counted[8],word_counted[9]))
            conn.commit()
        

    

with DAG(dag_id='csv_mysql',
        schedule_interval='@daily',
        default_args=default_args,
        catchup=False
)as dag:
    
    pt1 = PythonOperator(
    task_id="crawling_data",
    python_callable=crawling
    )
    pt2 = PythonOperator(
    task_id="Pre_processing",
    python_callable=Pre_processing 
    )
    pt3 = PythonOperator(
    task_id="save_to_csv",
    python_callable=save_to_csv 
    )
    pt4 = PythonOperator(
    task_id="save_to_mysql",
    python_callable=save_to_mysql
    )    


    pt1 >> pt2 >> pt3
    pt1 >> pt2 >> pt4
    
    
#pymysql -> host문제