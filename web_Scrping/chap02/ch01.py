from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

namelist = soup.find_all('span',{'class':'green'})
for name in namelist:
    print(name.text)

princelist = soup.find_all(text='the prince')
print(princelist)
print('the prince count : ', len(princelist))

table_tag = soup.find('table', {'id':'giftList'})
for child in table_tag.children:
    print(child)