from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\PythonHome\chromedriver.exe")
driver.get("https://www.pet-friends.co.kr/product/information?product_id=6627")

import time
wadiz_list = []
wadiz_body = []
wadiz_ = {}

table = driver.find_element_by_class_name("review-order-by-container")
rows = table.find_elements_by_class_name("review-item")

for i in range(1,5):
    table = driver.find_element_by_class_name('review-list')
    rows = table.find_elements_by_class_name("review-item")
    rows = table.find_elements_by_class_name("review-item")[i]
    rows.click()
    time.sleep(3)

    body = driver.find_elements_by_xpath(f'//*[@id="app"]/div[2]/div/div[6]/div[16]/div[3]/div[2]/div/div[1]/div[3]')
    for value in body:
        wadiz_body.append(value.text)
    wadiz_['body'] = wadiz_body

    time.sleep(2)
    button = driver.find_element_by_class_name('back-btn')
    button.click()
    time.sleep(2)
print(wadiz_)

import pandas as pd
import numpy as np
df1=pd.DataFrame(wadiz_)

import csv
df1.to_csv("wadiz.csv", mode='w',encoding='utf-8-sig')
