# step1.프로젝트에 필요한 패키지 불러오기
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
driver.get('https://www.ictintern.or.kr/homepage/trainingCompany/companyList.do')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
con = []
stack=[]
for m in range(1,10):
    driver.find_element_by_xpath(f'//*[@id="pagingNavi"]/div[2]/a[{m}]').click()

    try:
        for m in range(1,20):
            driver.find_element_by_xpath(f'//*[@id="container"]/form/div/div[3]/div[2]/table/tbody/tr[{m}]/td[3]/a').click()
            html=driver.page_source
            soup = BeautifulSoup(html,'html.parser')
    
            ht = soup.find_all('tbody')[4]
            com.append(ht.find_all('tr')[7].text)

            std_wokr = soup.find_all('tbody')[13]
            std_wokr_tr = std_wokr.find_all('tr')

            for work_j in std_wokr_tr[0].select('td div div div.item'):
                work.append(work_j.text)
            
            for stack_j in std_wokr_tr[1].select('td div div div.item'):
                stack.append(stack_j.text)

            driver.find_element_by_xpath(f'//*[@id="contents_area"]/div/div[3]/a').click()
    except:
        continue
driver.quit()

#%%

#%%
try:
    with open('com_info.txt', mode = 'w', encoding = 'utf-8') as f:
        for i in com:
            f.write(i)
except:
    pass

with open('work.csv', mode = 'w', encoding = 'utf-8') as f:
    for i in work:
        f.write(f"{i},")

with open('stack.csv', mode = 'w', encoding = 'utf-8') as f:
    for i in stack:
        f.write(f"{i},")

it_table2 = pd.DataFrame(stack)
print(it_table2.head()) 
it_table2.to_csv('it_table2.csv', encoding='utf-8', mode='w', index=True)

counts = Counter(result)
tags = counts.most_common(40)
print(tags)

if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin': # Mac OS
    path = r'/System/Library/Fonts/AppleGothic'
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

wc = WordCloud(font_path=path, background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))



plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()



