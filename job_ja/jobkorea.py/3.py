from bs4 import BeautifulSoup
from selenium import webdriver
import time
from konlpy.tag import Okt
from collections import Counter
import platform
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import pandas as pd

driver=webdriver.Chrome('chrome\chromedriver.exe')

driver.get('https://www.ictintern.or.kr/homepage/trainingCompany/companyList.do')


driver.find_element_by_xpath('//*[@id="S_PLAN_NO"]/option[3]').click()
driver.find_element_by_xpath('//*[@id="container"]/form/div/div[2]/div/a').click()


data_list=[]
stack=[]


for j in range(1,9) :
    driver.find_element_by_xpath(f'//*[@id="pagingNavi"]/div[2]/a[{j}]').click()
    time.sleep(0.5)

    # ============기술스택

    for m in range(1,21):
        driver.find_element_by_xpath(f'//*[@id="container"]/form/div/div[3]/div[2]/table/tbody/tr[{m}]/td[3]/a').click()
        html=driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        
        std_wokr = soup.find_all('tbody')[13]
        std_wokr_tr = std_wokr.find_all('tr')
        for stack_j in std_wokr_tr[1].select('td div div div.item'):
            stack.append(stack_j.text)
                      
        driver.find_element_by_xpath(f'//*[@id="contents_area"]/div/div[3]/a').click()


    # ============기술스택

    html=driver.page_source
    # print(html)
    soup = BeautifulSoup(html,'html.parser')
    # print(soup.find_all('table',{'class':'bbsViewB'}))
    all_div=soup.find_all('div',{'class':'selectize-input items not-full has-options has-items disabled locked'})
    for i in all_div:
        # print('-'*100)
        # print(i.text)
        data_list.append(i.text)
    print(len(data_list))

driver.quit()

print(stack)


try:
    with open('bigdata.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(data_list)
except:
    pass


try:
    with open('stack.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(stack)
except:
    pass


with open('bigdata.csv', 'r', encoding='utf-8') as f:
    list1 = csv.reader(f)
    list2 = list(list1)[0]
    # for line in data_list1:
        # data_list1.append(line)


print(list2)