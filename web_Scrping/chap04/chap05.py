from bs4 import BeautifulSoup # 크롤링을 하기 위해
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe')
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame('mainFrame') # 해당 iframe으로 이동
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
whole_border = soup.find('div', {'id': 'whole-border'})
results = whole_border.find_all('div', {'class': 'se-module'})

result1=[]
for result in results:
    print(result.text.replace('\n', ''))
    result1.append(result.text)