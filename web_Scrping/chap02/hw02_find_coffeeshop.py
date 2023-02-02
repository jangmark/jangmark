import pandas as pd

hollys_shop = pd.read_csv(r'D:\web_Scrping\hollys2.csv',encoding='utf-8')

while True:
    q = input("검색할 매장의 도시를 입력하세요 : ")
    if q == 'quit': 
        print("종료")
        break
    else:
        q_shop = hollys_shop.loc[hollys_shop["위치(시,구)"].str.contains(q)]
        print('-'*30)
        print('검색된 매장의 수 : ', len(hollys_shop))
        print('-'*30)
        for x in range(len(q_shop)):
            print(f'[{x+1}]: {q_shop.iloc[x,2]},{q_shop.iloc[x,3]}')
        print('-'*30)