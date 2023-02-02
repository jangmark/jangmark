from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
count = 0
def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text()) # <h1>태그 검색
        #print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='mw-content-text').find('p'))
        # 편집 버튼: <li id="ca-edit"> 태그에 존재
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('this page is missing something! Continuing: ')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'*40)
                count += 1
                print('[{0}]: {1}'.format(count, newPage))
                pages.add(newPage)
                getLinks(newPage)

getLinks('')