
from urllib.request import urlopen
from bs4 import BeautifulSoup

def scraping_use_find(html):
    html = urlopen(html)
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(f'[select 함수 사용]',end='\n')
    div_tags = bs.find_all('div',{'class':'tombstone-container'})
    print(f'총 tombstone-container 검색 개수 : {len(div_tags)}')

    allname = bs.find_all('div',{'class':'tombstone-container'})
    for x in allname:
        print('-------------------------------------------------------')
        print('[Period] : ',x.find('p',{'class':'period-name'}).text)
        print('[Short desc] :',x.find('p',{'class':'short-desc'}).text)
        print('[Temperature]:',x.find('p',{'class':'temp'}).text)
        print('[Image desc] :',x.find('img')['title'])    

    print('\n\n')

def scraping_use_select(html):
    html = urlopen(html)
    bs = BeautifulSoup(html.read(), 'html.parser')
    link = bs.select('div.tombstone-container')
    print(f'[select 함수 사용]',end='\n')
    div_tags = bs.select('div.tombstone-container')
    print(f'총 tombstone-container 검색 개수 : {len(div_tags)}')
    for x in link:
        print('---------------------------------------------------------')
        print('[Period] : ',x.select_one('p.period-name').text)
        print('[Short desc] : ',x.select_one('p.short-desc').text)
        print('[Temperature]:',x.select_one('p.temp').text)
        print('[Image desc] : ',x.select_one('img')['title'])


scraping_use_find('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY')
scraping_use_select('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY')





        




