from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


class naver_stock10:
    def __init__(self,html):
        self.html = html
        a = html
        self.html = requests.get(a) 
        self.soup = BeautifulSoup(self.html.text,'html.parser')
        self.top10_list = []   # list 생성
        self.top10_html = []
        top10 = self.soup.select('a.tltle')  # 회사명만 뽑아오기
        for i in range(10):
            self.top10_list.append(top10[i].text)             
            self.top10_html.append(top10[i]['href'])
        
        return self.company10()
    
    def company10(self):

        while True:
            print('[네이버 코스피 상위 10대 기업]')
            for x in range(len(self.top10_list)):
                print(f'{[x+1]} {self.top10_list[x]}')


            msg = int(input("주가를 검색할 기업의 번호를 입력하세요.(-1:종료) : "))
            if msg == -1:
                break

            elif 1 <= msg <= 12:
                html = urlopen(f'https://finance.naver.com/item/main.naver?code={self.top10_html[msg-1][-6:]}')
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
            


a = naver_stock10(r'https://finance.naver.com/sise/sise_market_sum.naver')
            
