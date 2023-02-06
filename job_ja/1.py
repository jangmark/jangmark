from bs4 import BeautifulSoup
from selenium import webdriver
import time
from konlpy.tag import Okt
from collections import Counter
import platform
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe')

work= []
stack = []

for i in range(1,5):
    driver.find_element_by_xpath(f'//*[@id="container"]/form/div/div[3]/div[2]/table/tbody/tr[{i}]/td[3]/a').click()
    html=driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    item = soup('tbody>tr>td>div>div')

    for n in item:
        print(n.find_all('div'))
        # stack.append(n.text)
    driver.find_element_by_xpath(f'//*[@id="contents_area"]/div/div[3]/a').click()

print(stack)

# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time

# driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe')
# driver.get('https://www.ictintern.or.kr/homepage/trainingCompany/companyList.do')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# driver.get('https://www.ictintern.or.kr/homepage/trainingCompany/companyList.do')
# driver.implicitly_wait(2)

# driver.find_element_by_xpath('//*[@id="WORK_CD_16"]').click()
# driver.implicitly_wait(2)

# driver.execute_script('btnSearch()')
# time.sleep(1)

# com, work, stack = [], [], []

# for _ in range(2):
#     html = driver.page_source
#     bs = BeautifulSoup(html, 'html.parser')

#     href_c = bs.select('.left a')
    
#     for i in href_c:
#         try:
#             script_url = i['href'].split(':')[1]
#             print('script_url: ', script_url)
#             driver.execute_script(script_url)
#             time.sleep(2)

#             html = driver.page_source
#             bs = BeautifulSoup(html, 'html.parser')

#             ht = bs.find_all('tbody')[4]
#             com.append(ht.find_all('tr')[7].text)

#             std_wokr = bs.find_all('tbody')[13]
#             std_wokr_tr = std_wokr.find_all('tr')

#             # 실습생 

#             # 실습생
#             for stack_j in std_wokr_tr[1].select('td div div div.item'):
#                 stack.append(stack_j.text)

#             driver.find_element_by_xpath('//*[@id="contents_area"]/div/div[3]/a').click()
#             time.sleep(2) 
        
#         except:
#             print(i['href'])
#             continue
#     driver.find_element_by_xpath(f'//*[@id="pagingNavi"]/div[2]/a[2]').click()
#     time.sleep(1)
#     print('-'*30)
# driver.quit()

# print(com)
# print(work)
# print(stack)