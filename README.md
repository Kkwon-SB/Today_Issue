<h4>
<a target="_blank" href="https://www.notion.so/2c6f5a2112364cc8b6b60e6b6341d70e">
   [배운 내용 & 트러블 슈팅]
</a>
</h4>

## 오늘 이슈
<pre>
<code>
<b>주제</b> : 데이터 파이프라인을 자동화하여 최신 이슈 정보를 추출하는 개인 프로젝트 입니다. </br>
<b>개발 기간</b> : '23.02.06 ~ '23.02.19</br></br>
</code>
</pre>

## 1. 소개

<b>진행 과정</b> : <br>
1. 웹 뉴스 기사 정보를 (Beautifulsoup)크롤링 후 전처리 및 wordcount를 통해 많이 언급된 단어 추출한다.<br>

2. (re)정규표현식 & (KoNLPy)형태소 분석 : 크롤링된 데이터에서 단어를 추출하여 가장 많이 언급된 단어 파악하자.<br>

3. mysq 데이터 입력 or csv파일로 저장<br>

3. 1 ~ 3 일련의 과정을 Airflow의 워크플로우 자동화를 통해 지속적인 작업이 가능하게끔 구현 한다.</br>

<img src="https://user-images.githubusercontent.com/76522430/220311923-97414f68-e459-4292-9ba4-d9622ee3b93c.png" width="600" height="200">

![image](https://user-images.githubusercontent.com/76522430/220312498-664a845c-9cb2-48ce-9641-0a227c75ebed.png)


#### 정상적인 파일 생성 및 데이터 입력 완료
![image](https://user-images.githubusercontent.com/76522430/220214659-82620066-032f-410c-83c7-fe6e36d8558e.png)

## 2. S/W architecture

**0.프로젝트 구조도**(수정필요)


## 3. 사용 기술🛠

**Environment**
   <table>
     <tr>
       <td><img src="https://user-images.githubusercontent.com/76522430/219982237-e0b5a7c4-73f3-4274-9ee9-ff8fcb336add.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/219982214-47103bf0-af0f-499d-b165-2b725b9b1ff6.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/219982269-70d12c5a-2491-4702-9cd4-f95d585918e7.png" width="100" height="100"></td>
       <td><img src="https://user-images.githubusercontent.com/76522430/219982070-a3a427b6-9789-4064-a0ec-070b704cac18.png" width="100" height="100"></td>
     </tr>
     <tr>
       <td align=center>Airflow</td>
       <td align=center>SQL & MYSQL</td>
       <td align=center>Python</td>
       <td align=center>BeautifulSoup</td>
     </tr>
   </table>
<br>

## 4. 결과
- 1위 ~10위 중 상위권에 가까울 수록 실제 관련 기사가 대부분이었다. 하지만 뒤로 갈 수록 판단하기 애매한 rank, 단어가 있었다. 

![image](https://user-images.githubusercontent.com/76522430/220311328-3f69ff28-e7ed-4e16-b1cf-c16e08887268.png)

<br>

<h4>
<a target="_blank" href="https://www.notion.so/2c6f5a2112364cc8b6b60e6b6341d70e">
   [배운 내용 & 트러블 슈팅]
</a>
</h4>
