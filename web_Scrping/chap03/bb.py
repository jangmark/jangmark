class tennisball:

    def __init__(self):
        self.main()

    def push(self):
        if len(self.case)==5:
            print('케이스가 꽉 찼습니다.')
        else:
            self.case.insert(0,len(self.case)+1)
            self.counting()

    def pop(self):
        if len(self.case)==0:
            print('케이스가 비어 있습니다.')
        else:
            print(f'Pop({len(self.case)})')
            self.case.remove(len(self.case))
            if len(self.case)==0:
                print('케이스가 비어 있습니다.')
            else:
                self.counting()

    def counting(self):
        print(f'[공의 개수]: {len(self.case)}')
        print(*self.case)

    def main(self):
        self.case=[]
        while True:
            print('-'*40)
            print('1. 테니스 공 넣기')
            print('2. 테니스 공 꺼내기')
            print('3. 테니스 공 개수 출력')
            print('4. 종료')
            menu=input('메뉴를 선택하세요: ')
            if menu in ['1','2','3','4']:
                menu=int(menu)
                if menu==4:
                    break
                elif menu==1:
                    self.push()
                elif menu==2:
                    self.pop()
                elif menu==3:
                    self.counting()
            else: print('잘못된 메뉴 선택입니다.')

ex=tennisball()