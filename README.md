<h4>
<a target="_blank" href="https://www.notion.so/2c6f5a2112364cc8b6b60e6b6341d70e">
   [배운 내용 & 트러블 슈팅]
</a>
</h4>

## 오늘의 이슈
<pre>
<code>
<b>데이터 파이프라인을 자동화하여 최신 이슈 정보를 추출하는 개인 프로젝트 입니다.</b></br>
<b>주제</b> : 언론사별 뉴스 기사 정보를 통해 최신 이슈 파악 </br>
<b>개발 기간</b> : '23.02.06 ~ '23.02.19</br></br>
</code>
</pre>

## 1. 소개

<b>진행 과정</b> : <br>
실시간 검색어를 대신할 수 있는, 최신 이슈를 한 눈에 보기 위해 뉴스 기사 데이터를 크롤링 후 wordcount를 통해 많이 언급된 단어 추출한다.<br>
bs4를 통해 웹 정보를 가져오고, re전처리 및 wordcount, mysql연동 & csv저장<br>
이와 같은 일련의 과정을 airflow의 워크플로우 자동화를 통해 지속적인 작업이 가능하게끔 구현 한다.</br>
빅데이터 구축 시 발생하는 비용 문제를 개선하고자 프로젝트를 진행했습니다.<br><br>


## 2. S/W architecture

**0.프로젝트 구조도**
<br>
<img width="750" alt="" src="https://user-images.githubusercontent.com/76522430/198029901-2f54ab0a-2024-4410-9015-2bee589b8dfe.png">

-   네임노드(instances 2개)
-   데이터노드(instances 3개)
-   MLflow(higher instance1개)
<!-- ![image](https://user-images.githubusercontent.com/76522430/198029901-2f54ab0a-2024-4410-9015-2bee589b8dfe.png) -->

**1.하둡**
<br>
<img width="600" alt="" src="https://user-images.githubusercontent.com/76522430/202516933-9f137909-d6bf-4ec2-ba3b-3a0853127c13.png">
<img width="600" alt="" src="https://user-images.githubusercontent.com/76522430/202517034-94db9866-2aa6-4014-90df-ee2b81f8a476.png">

-   저렴한 구축 비용과 비용 대비 빠른 데이터 처리
-   Fault tolerance 장애 대응에 강함
-   Block storage
    <br><br>

## 3. 사용 기술🛠

**Environment**

   <table>
     <tr>
       <td><img src="https://user-images.githubusercontent.com/76522430/198021898-f24ba09d-ce68-4e24-90e3-270474005a16.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/198022023-a9a60c8e-99c3-4617-8f31-d43f36c7c6c9.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/198022648-a500b32d-1cb3-4d05-a6e5-f237bb688706.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/198023323-77c9e225-df0c-4d70-8ed2-c469971c7885.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/198021555-0a36d140-73da-48ea-aa96-171633a9fe4a.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/198021660-c3e1dd6f-8458-41f3-8dc1-e339a1bbeb55.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/198021734-df31223a-0b68-461d-98d4-045ae4c03f6b.png" width="100" height="100"></td>
     </tr>
     <tr>
       <td align=center>Hadoop</td>
       <td align=center>Spark</td>
       <td align=center>Hive</td>
        <td align=center>ZooKeeper</td>
       <td align=center>Airflow</td>
       <td align=center>AWS S3</td>
       <td align=center>MLflow</td>
     </tr>
   </table>

<br>

## 4. 결과



<br>

<h4>
<a target="_blank" href="https://www.notion.so/2c6f5a2112364cc8b6b60e6b6341d70e">
   [배운 내용 & 트러블 슈팅]
</a>
</h4>
