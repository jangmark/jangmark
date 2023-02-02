# 1. 알파벳 빈도수 계산 및 그래프 출력 (딕셔너리 활용)
# - 제공된 loremipsum.txt 파일을 읽어서, 각 알파벳 소문자, 대문자의 빈도수를 따로 계산하
# 고 그 결과를 그래프로 출력하시오. (다른 파일도 읽어서 분석이 가능해야 됨)
# - 숫자, 공백, 마침표 등 다른 문자들은 계산하지 않음
# - isalpha(), isdigit(), isspace()등 활용
# - str.islower(): 문자열이 소문자이면 True
# - str.isupper(): 문자열이 대문자이면 True
# - 빈도수가 0인 알파벳은 출력하지 않음
# - 알파벳 소문자, 대문자 빈도수를 각각 계산해서 아래의 그래프 출력
# - 출력은 빈도수가 제일 높은 문자부터 화면 출력함 (내림차순 정렬)


# 실행 결과 예시
# Input file name: loremipsum.txt
# 대문자:
# {'I': 6, 'L': 5, 'A': 1, 'P': 1, 'M': 1}
# 소문자:
# {'e': 59, 't': 43, 's': 39, 'n': 38, 'i': 32, 'a': 28, 'o': 25, 'r': 24, 'm':
# 18, 'p': 18, 'u': 17, 'l': 17, 'd': 16, 'h': 14, 'y': 000000000000000000000000000000000000000000000000000013, 'g': 11, 'c': 10, 'k':
# 7, 'f': 6, 'w': 6, 'b': 5, 'v': 5, 'x': 2}
# loremipsum_count.png is saved.

# Input file name: python.txt
# 대문자:
# {'P': 21, 'I': 8, 'C': 8, 'A': 5, 'M': 3, 'T': 2, 'D': 1, 'G': 1, 'R': 1, 'H':
# 1, 'F': 1, 'J': 1, 'L': 1, 'W': 1, 'K': 1, 'B': 1, 'O': 1}
# 소문자:
# {'e': 161, 't': 139, 'a': 126, 'n': 121, 'o': 117, 'r': 97, 's': 85, 'i': 81,
# 'l': 59, 'h': 57, 'm': 57, 'g': 50, 'd': 50, 'p': 42, 'u': 39, 'c': 35, 'y': 34,
# 'f': 23, 'k': 11, 'b': 10, 'w': 9, 'v': 9, 'j': 2, 'z': 2, 'x': 1, 'q': 1}
# python_count.png is saved.

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def readtext(filename):

    f = open(filename,'r',encoding='utf-8')
    text = f.read()

    uptext = {}
    lowertext = {}

    for x in text:
        if 65 <= ord(x) <= 91:
            if x in uptext.keys():
                uptext[x] += 1
            else: 
                uptext[x] = 1
    
    
        elif 97 <= ord(x) <= 123:
            if x in lowertext.keys():
                lowertext[x] += 1
            else: 
                lowertext[x] = 1

    print(f'대문자 : {uptext}')
    print(f'소문자 : {lowertext}')


    sorted_updict = dict(sorted(uptext.items(), key = lambda x:x[1], reverse=True))
    sorted_lowerdict = dict(sorted(lowertext.items(), key = lambda x:x[1], reverse=True))
    
    print(f'대문자 : {sorted_updict}',end='\n\n')
    print(f'소문자 : {sorted_lowerdict}',end='\n\n')
    print(sorted_updict.keys)
    
    fig = plt.figure(figsize=(10,5))
    axes1 = fig.add_subplot(2,2,1)
    axes2 = fig.add_subplot(2,2,2)
    axes1.bar(sorted_updict.keys(),sorted_updict.values(),data=dict,)
    axes2.bar(sorted_lowerdict.keys(),sorted_lowerdict.values(),data=dict)
    axes1.set_xlabel('alphabet')
    axes1.set_ylabel('Count')
    axes1.set_title('대문자의 개수')
    axes2.set_xlabel('alphabet')
    axes2.set_ylabel('Count')
    axes2.set_title('소문자의 개수')
    
    plt.show()

readtext(r'C:\Users\장마가\Desktop\SQL\loremipsum.txt')
readtext(r'C:\Users\장마가\Desktop\SQL\python.txt')

    
