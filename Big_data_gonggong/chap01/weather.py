#%%
import csv
import matplotlib.pyplot as plt
import platform
import matplotlib.font_manager as fm
system_name = platform.system()
if system_name == 'Windows':
# Windows 운영체제
    print('Windows OS')
    plt.rc('font', family='Malgun Gothic')
elif system_name == 'Darwin': # Mac OS
    print('Mac OS')
    plt.rc('font', family='AppleGothic')
elif system_name == 'Linux': # Linux
    print('Linux OS')
    path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
    font_name = fm.FontProperties(fname=path, size=12)
    plt.rc('font', family=font_name)
else:
    print("Not support")


    # for i in range(start,end):
    #     m=mon[mon['날짜'].dt.year==i]
    #     max_temp.append(round(m['최고기온'].mean(),1))
    #     min_temp.append(round(m['최저기온'].mean(),1))
    # print(f'{start}년부터 {end}년까지 {month}월의 기온 변화\n')
    # print(f'{month}월 최저기온 평균 : ')
    # print(str(min_temp)[1:-1])
    # print(f'{month}월 최고기온 평균 : ')
    # print(str(max_temp)[1:-1])


def weather(startyear, endyear, month):

    f = open('daegu_utf8.csv', encoding='utf-8')
    data = csv.reader(f)
    next(data)
    startyear = int(input("시작년도"))
    endyear = int(input("끝나는 년도"))
    month = int(input('측정할 달'))

    high_temp = [] # 최고 기온을 저장할 리스트
    low_temp = [] # 최저 기온을 저장할 리스트
    x_year = [] # x축 연도를 저장할 리스트

    for row in range(startyear,endyear):


 



 

 
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic', size=8)
    else:
        plt.rc('font', family='AppleGothic', size=8) # 한글 폰트 사용 For Mac OS
    
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("{0}년 이후 {1}년까지 {2}월의 기온 변화".format(startyear, endyear, month),size=16)
    
    plt.legend(loc=2)
    plt.show()

weather(startyear, endyear, month)

# weather(startyear,endyear,month)
#%%

import csv
import matplotlib.pyplot as plt
import platform
import matplotlib.font_manager as fm
system_name = platform.system()
import pandas as pd

def s_e_m():
    start=int(input('시작 연도를 입력하세요 : '))
    end=int(input('마지막 연도를 입력하세요 : '))
    month=int(input('기온 변화를 측정할 달을 입력하세요 : '))
    
    daegu=pd.read_csv('daegu-utf8.csv',encoding='utf-8-sig')
    daegu.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']
    daegu['날짜']=pd.to_datetime(daegu['날짜'], format='%Y-%m-%d')
    
    year = daegu[(daegu['날짜'].dt.year >= start) & (daegu['날짜'].dt.year <= end)]
    mon = year[year['날짜'].dt.month == month]
    
    x_year=[i for i in range(start,end)]
    max_temp=[]
    min_temp=[]
    for i in range(start,end):
        m=mon[mon['날짜'].dt.year==i]
        max_temp.append(round(m['최고기온'].mean(),1))
        min_temp.append(round(m['최저기온'].mean(),1))
    print(f'{start}년부터 {end}년까지 {month}월의 기온 변화\n')
    print(f'{month}월 최저기온 평균 : ')
    print(str(min_temp)[1:-1])
    print(f'{month}월 최고기온 평균 : ')
    print(str(max_temp)[1:-1])
    
    plt.figure(figsize=(20, 4))
    plt.plot(x_year,max_temp, 'red', marker='o', label='최고기온')
    plt.plot(x_year,min_temp, 'blue', marker='s', label='최저기온')

    if platform.system()=='Windows':
        plt.rc('font',family='Malgun Gothic',size=8)
    else:
        plt.rc('font',family='AppleGothic', size=8)

    plt.rcParams['axes.unicode_minus'] = False 
    plt.title(f"{start}년부터 {end}년까지 {month}월의 기온 변화",size=16)
    plt.xticks(x_year)
    plt.legend(loc='best')
    plt.show()
s_e_m()