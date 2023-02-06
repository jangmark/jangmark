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
result = []

for i in range(1,10):
    driver.find_element_by_xpath(f'//*[@id="pagingNavi"]/div[2]/a[{i}]').click()
    time.sleep(1)
    item = soup.select('tbody>tr>td>a>p>div>div>div')
    for x in item:
        result.append(x.text)


print(result)

it_table = pd.DataFrame(result)
print(it_table.head()) 
it_table.to_csv('it_table.csv', encoding='utf-8', mode='w', index=True)

counts = Counter(result)
tags = counts.most_common(40)[1:]
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



# step2.로그인 정보 및 검색할 회사 미리 정의, 해당 회사의 리뷰 끝 페이지도 정의
