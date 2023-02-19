from datetime import datetime
from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_args = {
    'start_date' : datetime(2023, 2, 2),
}


# sql_create_table = """
#     CREATE TABLE IF NOT EXISTS `mydatabase`.`sqlllT2` (
#         `id` INT NOT NULL AUTO_INCREMENT,
#         `count` INT,
#         PRIMARY KEY (`id`));


#  `date_time` VARCHAR(45),
#    `2nd` VARCHAR(45),
#         `3rd` VARCHAR(45),
#         `4th` VARCHAR(45),
#         `5th` VARCHAR(45),
#         `6th` VARCHAR(45),
#         `7th` VARCHAR(45),
#         `8th` VARCHAR(45),
#         `9th` VARCHAR(45),
#         `10th` VARCHAR(45),
sql_create_table = """
    CREATE TABLE IF NOT EXISTS `mydatabase`.`hot_topic_keyword12222` (
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
now_time = datetime.now()
num1 = 'kwon'
num2 = 'kwon2'
num3 = 'kwo34'
num4 = 'kwon4'
num5 = 'kwon5'
num6 = 'kwon6'
num7 = 'kwon7'
num8 = 'kwon8'
num9 = 'kwon9'
num10 = 'kwon10'

sql_insert_data = f"insert into `hot_topic_keyword12222`(`1st`,`2nd`,`3rd`,`4th`,`5th`,`6th`,`7th`,`8th`,`9th`,`10th`) values ('{num1}','{num2}','{num3}','{num4}','{num5}','{num6}','{num7}','{num8}','{num9}','{num10}')"
# f"insert into sql_test_ST(NAME) values ('{name}');"   
with DAG(dag_id='test_sql',
        schedule_interval='@daily',
        default_args=default_args,
        tags=['test_sql'],
        catchup=False) as dag:
    
    t1 = MySqlOperator(
        task_id='creating_table',
        mysql_conn_id='mysql_home',
        sql="""
                CREATE TABLE IF NOT EXISTS `mydatabase`.`hot_topic_keyword12222` (
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
    
    t2 = MySqlOperator(
        task_id='insert_date',
        mysql_conn_id='mysql_home',
        sql=sql_insert_data
    )
    
    t1 >> t2