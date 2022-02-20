from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\PythonHome\chromedriver.exe")
driver.get("https://www.pet-friends.co.kr/main/tab/2")

import time
coment = []
time.sleep(40)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
for c in range(10):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

for i in range(1,5):
    body = driver.find_elements_by_xpath(f'//*[@id="app"]/div[2]/div/div[4]/div/div[4]/div[2]/div/div[{i}]/div[3]')
    for value in body:
        coment.append(value.text)

print(coment)

import pandas as pd
import numpy as np
df1=pd.DataFrame(coment)

import csv
df1.to_csv("petfriend_테스트.csv", mode='w',encoding='utf-8-sig')
