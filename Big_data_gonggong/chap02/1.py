#%%
# 데이터 헤더
import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
print(header)
i = 1
for row in data:
    print(row)
    if i > 5:
        break
    i += 1
f.close()

# %%
# 전체 탑승 인원 대비 유임 승차 비율이 가장 높은 역은?
# 유임 승차 대 무임 승차 비율 (rate) 계산

import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
max_rate = 0
rate = 0

for row in data:
    for i in range(4,8):
        row[i] = int(row[i]) # 4, 5, 6, 7 컬럼값을 정수로 변환
    rate = row[4] / (row[4] + row[6]) # [6]컬럼의 값이 0인 행 확인 용도
    if row[6] == 0: # 무임승차 인원[6]이 없는 역 출력
        print(row)
f.close()
# %%
# 무임승차 인원이 0인 역 찾기 #1
import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate =0
rate = 0
i = 0

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i]) # 4, 5, 6, 7 컬럼값을 정수로 변환
    if row[6] != 0:
# 무임 승차 (%) = (무임 승차 수 x 100) / (유임 승차 수 + 무임 승차 수)
        rate = (row[6] * 100) / (row[4] + row[6])
        if rate > max_rate:
            max_rate = rate
            print(row, round(rate, 2), '%')

f.close()
# %%
import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)

max_rate = 0
rate = 0
max_row = []
total_count = 0
max_total_num = 0

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    total_count = row[4] + row[6] # 유임승차수 + 무임승차수
    if (row[6] !=0) and (total_count >100000) :
        rate = row[4] / total_count
    if rate > max_rate :
        max_rate = rate
max_row = row
max_total_num = total_count

print(max_row)
print("역이름: {0}, 전체 인원: {1:,}, 유임승차인원: {2:,}, 유임승차 비율: {3:,}".
format(max_row[3], max_total_num, max_row[4], round(max_rate*100, 1)))
f.close()
# %%

import matplotlib.pyplot as plt

plt.pie([10,20])
plt.show()
# %%
import  matplotlib.pyplot as plt
import platform

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else: # MacOS: ‘Darwin’
    plt.rc('font', family='AppleGothic')

numbers = [214, 2312, 1031, 1233]
blood_type = ['A형', 'B형', 'AB형', 'O형']
plt.axis('equal') # 파이 차트를 원형으로 그려줌
plt.pie(numbers, labels=blood_type, autopct='%.1f%%')
plt.legend()
plt.show()

# %%
import csv
import matplotlib.pyplot as plt
import platform

f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
print(header)
min_rate = 100
rate = 0
min_row = []
total_count = 0
min_total_count = 0
for row in data:
    for i in [4,6]:
        row[i] = int(row[i])
    total_count = row[4] + row[6]
    
# 무임승차 인원이 없고, 총 승차인원이 1만명 이상
if (row[6] != 0) and (total_count >= 10000):
    rate = row[4] / total_count
    if rate <= 0.5:
        print(row, round(rate, 2))
        if rate < min_rate:
            min_rate = rate
            min_row = row
            min_total_count = total_count

print('유임 승차 비율이 가장 낮은 역: {0}, 전체 인원:{1:,}명,유임승차인원:{2:,}명, 유임승차비율:{3:,}%'.format(min_row[3], min_total_count,min_row[4], round(min_rate*100, 1)))

f.close()

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')
    
plt.title(min_row[3] + " 유,무임 승차 비율")
label = ['유임승차', '무임승차']
values = [min_row[4], min_row[6]]

plt.pie(values, labels=label, autopct='%.1f%%')
plt.show()
# %%
import csv
max = [0] * 4 # [0]: 최대 유임승차,[1]: 최대 유임하차, [2]: 최대 무임승차, [3]: 최대 무임하차
max_station = [''] * 4
label = 
# with 구문: 자동으로 파일을 close()시킴
with open('subwayfee.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        for i in range(4, 8):
            row[i] = int(row[i])
            if row[i] > max[i-4]: # 원본데이터의 컬럼 (인덱스 -4) -> max리스트의 인덱스
                max[i-4] = row[i]
                max_station[i-4] = row[3] + ' ' + row[1] # '역이름 지하철노선' 추가

for i in range(4):
    print('{0}: {1} {2:,}명'.format(label[i], max_station[i], max[i]))