# 1. 커피 자판기 프로그램. (제출 파일명: vendingmachine.py)
# n 아래 기능을 각각 함수로 구현하세요.
# n 화면상에 메뉴를 출력함 (종료를 선택할 때까지 반복, while문 사용)
# - 1. 블랙커피, 2: 프림커피, 3: 설탕프림 커피, 4: 재고현황, 5: 종료
# - 커피 가격은 모두 300원으로 동일함
# n 초기 자판기 상황
# - 자판기 동전: 10,000원 (모두 100원짜리 100개 보유)
# - 물: 1000ml
# - 커피: 500g, 프림: 500g, 설탕: 500g, 종이컵 30개
# n 메뉴에 따른 커피, 설탕, 프림 소모량
# - 블랙커피: 커피 30g + 물 100ml
# - 프림커피: 커피 15g + 프림 15g + 물 100ml
# - 설탕커피: 커피 10g + 프림 10g + 설탕 10g + 물 100ml
# n 재고현황
# - 커피 재고량, 프림 재고량, 설탕 재고량, 컵 재고량, 잔여 물용량 출력
# - 잔돈 현황 출력 (입출금 관리)
# n 소스 상단에 반드시 주석으로 학번, 이름 추가할 것

# class coffee:

#     def coiniput(self.):

#         coin = 10000
#         water,coffee, prim,sugar,cup = 1000,500,500,500,30
#         blackcoffee : {coffee : 30, water : 100 }
#         primcoffee : {coffee : 15, prim : 15, water : 100 }
#         sugarcoffee : {coffee : 10, prim : 15, sugar : 10 ,water : 100 }

#         while True:
#             m = int(input("동전을 투입하세요 : "))
#             if m < 300:
#                 print(f'돈이 부족합니다. {m}')
#                 print("-------------------")
#                 print("커피 자판기 동잔을 종료합니다.")
#                 break

#             if m >= 300:
#                 print('---커피 판기기 (300원)---')
#                 print('1. 블랙 커피')
#                 print('2. 프림 커피')
#                 print('3. 설탕 프림 커피')
#                 print('4. 재고 현황')
#                 print('5. 종료')
#                 menu=int(input('메뉴를 선택하세요: '))
            
#                 if menu = 1 or 2 or 3:
#                     if blackcoffee.items <= 



movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank[1] = '장마가'
print(movie_rank)

del movie_rank[2]

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

lang1.append(lang2)