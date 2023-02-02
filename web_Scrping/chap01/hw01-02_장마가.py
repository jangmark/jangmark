from urllib.request import urlopen
from bs4 import BeautifulSoup

def scraping_use_naver(html):
    html = urlopen(html)
    bs = BeautifulSoup(html.read(), 'html.parser')

    print('현재 위치: ',bs.select_one('h2.title').text)
    print('현재 온도: ',bs.select_one('div.temperature_text').text)
    print('날씨 상태: ',bs.select_one('span.weather').text)
    print('공기상태 : ')
    air = bs.select_one('ul.today_chart_list')
    for x in air:
        print(x.text.strip(),sep='\n')

    
    print('-------------------------')
    print('시간대별 날씨 및 온도')
    print('-------------------------')

    time_temp=bs.select('div.graph_inner li')
    for t in time_temp:
        print(t.text)
    

def scraping_use_google(html):
    html = urlopen(html)
    bs = BeautifulSoup(html.read(), 'html.parser')

    print('현재 위치 : ', bs.find('h2',{'class':'title'}).text)
    print('현재 온도 : ', bs.find('div',{'class':'temperature_text'}).text)
    print('날씨 상태 : ', bs.find('span',{'class':'weather before_slash'}).text)
    print('공기상태 : ')
    air = bs.find('ul',{'class':'today_chart_list'})
    for x in air:
        print(x.text.strip())

    print('-------------------------')
    print('시간대별 날씨 및 온도')
    print('-------------------------')

    weather = bs.find('div',{'class':'graph_inner _hourly_weather'}).find_all('li')
    for y in weather:
        print(y.text)


    
    
scraping_use_naver('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')
scraping_use_google('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')
