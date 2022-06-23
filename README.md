![header](https://capsule-render.vercel.app/api?type=slice&color=80d8ff&height=250&section=header&text=Image%20crawling&fontSize=50&animation=fadeIn&fontAlignY=50&desc=Joan%20&descAlignY=62&descAlign=62&)

<div align="center">
 
![image](https://user-images.githubusercontent.com/106906742/175289294-a655a4c8-5808-4d81-9251-640f4c6447c5.png)
 
### :speaker: 개발 목표 :speaker:
Venv를 통해 파이썬 가상 환경 세팅 후 Selenium과 크롬드라이버를 이용해</br>
구글 사이트 이미지 크롤링 기능을 구현한다.


### :page_with_curl: 사용 기술 :page_with_curl:

<img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/-Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=black"/>

### :point_right: 개발 환경 세팅 :point_left:

**[venv 가상 환경 생성]**</br>
python -m venv selenium</br>
(해당 프로젝트 경로 터미널에서 명령어 입력)

**[가상 환경 실행하기]**</br>
selenium\Scripts\activate

**[selenium 설치하기]**</br>
pip install selenium</br>
(pip 버전이 낮아 설치 실패하여 현재 경로에서 바로 업데이트 해줌.</br>
=> 업데이트 명령어 : python -m pip install --upgrade pip)

**[구글 드라이버 설치]**</br>
1.Chromedriver 검색.</br>
2.https://chromedriver.chromium.org/downloads 에</br>
접속하여 맞는 버전을 윈도우 버전으로 다운로드.</br>
3.압축을 푼 후 안에 있는 chromedriver.exe 를 'selenium' 폴더안에 넣기.</br>
