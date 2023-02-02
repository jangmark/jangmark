# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pandas as pd
# result = []

# for n in range(1,54):
#     html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={n}&sido=&gugun=&store=')
#     bs = BeautifulSoup(html, 'html.parser')
#     link = bs.select('tbody>tr>td')
    
#     for x in link:
#         result.append(x.text)
#         loc = result[::6]
#         name = result[1::6]
#         juso = result[3::6]
#         phone = result[5::6]

# pd_table = pd.DataFrame({'매장이름' : name, '위치(시,구)' : loc, '주소': juso, '전화번호' : phone})
# pd_table.to_csv('hollys2.csv', encoding='utf-8', mode='w', index=True)

# for y in range(len(name)):
#     print(f'[{y+1}], 매장이름 : {name[y]}, 지역 : {loc[y]}, 주소 : {juso[y]}, 전화번호 : {phone[y]}')

import requests
from bs4 import BeautifulSoup

url = "https://www.jobkorea.co.kr/recruit/joblist?ct=0300&cg=0300&pg=1"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

jobs = soup.find_all('div', {'class': 'recruitment-items'})
for job in jobs:
    title = job.find('a', {'class': 'job-title'}).text.strip()
    company = job.find('div', {'class': 'recruit-company'}).text.strip()
    location = job.find('div', {'class': 'recruit-location'}).text.strip()
    print(title, company, location)


