# step1.프로젝트에 필요한 패키지 불러오기
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from konlpy.tag import Okt
from collections import Counter
import platform
from wordcloud import WordCloud
import matplotlib.pyplot as plt
driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe')
driver.get('https://www.ictintern.or.kr/homepage/trainingCompany/companyListDetail.do')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
result = []
a = soup.select('tbody>tr>td>div>div>div')
for x in a:
    result.append(x.text)

print(result)

# std_wokr = bs.find_all('tbody')[13]
# h = std_wokr.find_all('tr')
# for i in range(len(h)):
#     print(f"{'-' * 100} [{i:2}]")
#     print(h[i].text)

# work = [i.text for i in h[0].select('td div div div')]