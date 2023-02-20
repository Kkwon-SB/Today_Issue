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

for word in titles: #글자 수 설정, 단어 수 count
    if len(word) <= 1:
        continue
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
    
# word_counts = sorted(word_counts, key=lambda x: word_counts[x], reverse=True)[:10]
# word_counts = 'a','aa','aa','aaaa','aaaa','ba','ca','ad','ea','fa',

name = '홍길동'
sql_insert_data = f"insert into `sql_table`(`name`) values ('{name}')"


with DAG(dag_id='hot_topic_to_mysql',
        schedule_interval='*/30 * * * *',
        default_args=default_args,
        tags=['Daily','hot topic','news title crawling'],
        catchup=False
)as dag:
    st1 = MySqlOperator(
        task_id='creating_table',
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
        task_id='insert_task',
        mysql_conn_id='mysql_home',
        sql=sql_insert_data
    )
    
    st1 >> st2
    
#유니코드 에러 발생