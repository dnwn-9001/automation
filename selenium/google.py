from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

driver = webdriver.Chrome() # 다운 받아놓은 chromedriver.exe 불러오기
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q") # 검색창 요소 가져오기
elem.send_keys("웰시코기 꼬리 짧은 이유333")
elem.send_keys(Keys.RETURN) # RETURN : 엔터키

SCROLL_PAUSE_TIME = 1

# Get scroll height, 브라우저의 높이 가져오기
# execute_script : 자바스크립트 코드를 실행시키는 코드
last_height = driver.execute_script("return document.body.scrollHeight")


while True:
    # Scroll down to bottom / 브라우저 끝까지 스크롤 내림.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # driver.find_element_by_css_selector(".mye4qd").click()
        try:
            driver.find_element(By.CLASS_NAME, "mye4qd").click()
        except:
            break
    last_height = new_height


count = 1
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
for image in images : 
    try:
        image.click()
        time.sleep(3)
        imgUrl =driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + "cogi.png")
        count = count +1
    except:
        pass


driver.close()