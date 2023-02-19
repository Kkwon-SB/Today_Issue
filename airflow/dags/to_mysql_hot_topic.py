from datetime import datetime
from airflow import DAG
from bs4 import BeautifulSoup
import requests
import re
import csv
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_args = {
    'start_date' : datetime(2023, 2, 2),
}

aaa = ''
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
        
    # global num1, num2, num3, num4, num5, num6, num7, num8, num9, num10
    # num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = 'a','a','a','a','a','a','a','a','a','a'
    word_counts2 = sorted(word_counts,key=lambda x:word_counts[x], reverse=True)[:10]
    # num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = [i for i in word_counts2]
    context['task_instance'].xcom_push(key='processed_count_value', value=word_counts2)
    # print(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
    return 

# num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = 'a','a','a','a','a','a','a','a','a','a'
sql_insert_data = f"insert into `sql_test000`(`1st`,`2nd`,`3rd`,`4th`,`5th`,`6th`,`7th`,`8th`,`9th`,`10th`) values ('{num1}','{num2}','{num3}','{num4}','{num5}','{num6}','{num7}','{num8}','{num9}','{num10}')"



with DAG(dag_id='to_mysql_hot_topic',
        schedule_interval='*/30 * * * *',
        default_args=default_args,
        tags=['Daily','hot topic','news title crawling'],
        catchup=False
)as dag:
    
    pt1 = PythonOperator(
    task_id="crawling_news_title",
    python_callable=crawling
    )
    pt2 = PythonOperator(
    task_id="processing_count",
    python_callable=processing_count 
    )
    st1 = MySqlOperator(
        task_id='creating_table1',
        mysql_conn_id='mysql_home',
        sql="""
                CREATE TABLE IF NOT EXISTS `mydatabase`.`sql_test000` (
                    `cnt` INT NOT NULL AUTO_INCREMENT,
                    `1st` VARCHAR(45),
                    `2nd` VARCHAR(45),
                    `3rd` VARCHAR(45),
                    `4th` VARCHAR(45),
                    `5th` VARCHAR(45),
                    `6th` VARCHAR(45),
                    `7th` VARCHAR(45),
                    `8th` VARCHAR(45),
                    `9th` VARCHAR(45),
                    `10th` VARCHAR(45),
                    PRIMARY KEY (`cnt`));
            """
    )    
    st2 = MySqlOperator(
        task_id='insert_data',
        mysql_conn_id='mysql_home',
        sql=sql_insert_data
    )  
    
    pt1 >> pt2 >> st2
    st1 >> st2