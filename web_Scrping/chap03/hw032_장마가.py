from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html = requests.get(r'https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html.text, 'html.parser')

def naver():

    link = soup.select('a.tltle')
    top10 = []
    top10_http = []

    for x in range(10):
        top10.append(link[x].text)
        top10_http.append(link[x]['href'])

    while True:
        print('[네이버 코스피 상위 10대 기업]')
        for x in range(len(top10)):
            print(f'{[x+1]} {top10[x]}')

        msg = int(input("주가를 검색할 기업의 번호를 입력하세요.(-1:종료) : "))
        if msg == -1:
            break
        elif 1 <= msg <= 12:
            html = urlopen(f'https://finance.naver.com/item/main.naver?code={top10_http[msg-1][-6:]}')
            bs = BeautifulSoup(html, 'html.parser')
            con = bs.find('dl',{'class':'blind'})
            result = con.find_all('dd')
            g = bs.find('span',{'class':'code'}).text
            a = result[1].text.replace("종목명","종목명 : ")
            b = result[4].text.replace("현재가","헌재가 : ")
            c = result[5].text.replace("전일가","전일가 : ")
            d = result[6].text.replace("시가","시가 : ")
            e = result[7].text.replace("고가","고가 : ")
            f = result[9].text.replace("저가","저가 : ")

            print('-'*30)
            print('종목코드 :',g)
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            print(f)
            print('-'*30)

naver()

# https://finance.naver.com/item/main.naver?code=005930
# 종목명: 삼성전자
# 종목코드: 005930
# 현재가: 61,300
# 전일가: 61,800
# 시가: 61,800
# 고가: 62,200
# 저가: 61,200