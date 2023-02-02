from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

pages = set() # 세트 선언
count = 0
def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
    # 새로운 페이지 발견
                newPage = link.attrs['href']
                global count 
                count += 1
                print('[{0}]: {1}'.format(count, newPage))
                pages.add(newPage)
                getLinks(newPage)

getLinks('')

