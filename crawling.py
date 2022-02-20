from selenium import webdriver
import pandas as pd
import csv
import time

# 크롬드라이버 실행파일 절대주소 입력
driver = webdriver.Chrome(executable_path=r"C:\PythonHome\chromedriver.exe")
# 크롤링할 페이지의 url 입력
driver.get("https://www.pet-friends.co.kr/main/tab/2")

# 댓글들을 담을 리스트 생성
coment = []
time.sleep(40)

# 자동으로 스크롤 바 내리기(맨 밑까지 내릴려면 while True: 사용)
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
for c in range(10):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

# 크롤링할 댓글 수 range(m, n) -> m - n개
for i in range(1,5):
    body = driver.find_elements_by_xpath(f'//*[@id="app"]/div[2]/div/div[4]/div/div[4]/div[2]/div/div[{i}]/div[3]')
    for value in body:
        coment.append(value.text)

# 크롤링이 되었는지 확인
print(coment)

# 크롤링한 댓글들 dataframe에 넣기
df1=pd.DataFrame(coment)

# dataframe csv파일 생성
df1.to_csv("petfriend_테스트.csv", mode='w',encoding='utf-8-sig')
