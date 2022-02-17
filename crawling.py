from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\PythonHome\chromedriver.exe")
driver.get("https://www.pet-friends.co.kr/product/review/list?product_id=6627&package_code=N&is_user_product_review_writable=false")

import time
wadiz_list = []
wadiz_body = []
wadiz_ = {}

time.sleep(30)

for i in range(1,3):

    body = driver.find_elements_by_xpath(f'//*[@id="app"]/div[2]/div/div[4]/div/div[4]/div[2]/div/div[1]')
    for value in body:
        wadiz_body.append(value.text)
    wadiz_['body'] = wadiz_body

print(wadiz_)

import pandas as pd
import numpy as np
df1=pd.DataFrame(wadiz_)

import csv
df1.to_csv("petfriend.csv", mode='w',encoding='utf-8-sig')
