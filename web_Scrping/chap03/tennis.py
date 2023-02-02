# 1. 테니스 공 넣기 (클래스로 구현)
# 테니스 공 케이스에는 최대 5개의 테니스 공을 넣을 수 있음 (1차원 배열 사용).
# 파이썬에서 제공하는 pop() 함수는 사용할 수 없음.
# 1~4번 이외의 메뉴를 선택한 경우 "잘못된 메뉴 선택입니다." 출력함
# 메뉴 구성 (무한 반복: 4번 입력시 프로그램 종료)
# 1. 테니스 공 넣기 함수 구현 (push 함수 구현)
# - 숫자를 1부터 증가시키면서 추가함
# - 공을 넣고 top은 증가함
# - 화면에 현재 케이스의 상황을 출력함 (3번 함수 호출)
# - 공을 더 넣을 공간이 없는 경우(케이스의 최대 용량 이상) "케이스가 꽉 찼습니다." 출력
# 2. 테니스 공 꺼내기 함수 구현 (pop 함수 구현)
# - 테니스 공 케이스에서 하나씩 꺼내고 top은 감소함
# - 화면에 현재 케이스의 상황을 출력함 (3번 함수 호출)
# - 테니스 공 케이스에 공의 개수가 0개 이면(top==-1) "케이스가 비어있습니다." 출력
# 3. 테니스 공 개수 출력
# - 현재 케이스에 남아 있는 공의 개수 출력
# - 위에서 부터(top부터) 공의 정보 출력: 5 4 3 2 1 순서로 출력
# 4. 종료
# - 4번을 입력하면 프로그램 종료

class Tennis:

    def __init__(self):
        self.tennis_ball = 0
        self.tennis_list = []
        return self.menu()

    # 공 넣기 함수 --------------------------------------------------------------
    def push(self):
        if len(self.tennis_list) < 5: # 5보다 적을 때까지. 
            self.tennis_ball +=1
            self.tennis_list.append(self.tennis_ball)
            # for x in self.tennis_list[::-1]:
            #     print(x,end=" ")
            return self.check() 
        
        elif len(self.tennis_list) == 5:
            print('케이스가 꽉 찼습니다.')
            return self.menu()

    # 공 꺼내기 함수 --------------------------------------------------------------
    def pull(self):
        if len(self.tennis_list) <= 5:
            del self.tennis_list[-1]
            self.tennis_ball -=1   
            # for x in self.tennis_list[::-1]:
            #     print(x,end=" ")
            return self.check() 
        
        # elif len(self.tennis_list) == 0:
        #     print('케이스가 비어있습니다.')
        #     return self.menu()

    # 공 확인 함수 ----------------------------------------------------------------
    def check(self):
        if len(self.tennis_list) > 0:
            print('공의 개수 : ',len(self.tennis_list))
            for x in self.tennis_list[::-1]:
                print(x,end=" ")
            return self.menu()

        elif len(self.tennis_list) == 0:
            print('케이스가 비어있습니다.')
            return self.menu()

# 1~4번 이외의 메뉴를 선택한 경우 "잘못된 메뉴 선택입니다." 출력함
# 메뉴 구성 (무한 반복: 4번 입력시 프로그램 종료)

    def menu(self):

        print(" ")
        print('-------------------------------')
        print('1. 테니스 공 넣기')
        print('2. 테니스 공 빼기')
        print('3. 테니스 공 개수 출력')
        print('4. 종료')

        n = int(input("메뉴를 선택해주세요 : "))
        if n == 1:
            return self.push()
        elif n == 2:
            return self.pull()
        elif n == 3:
            return self.check()
        elif n == 4:
            return
        
        else:
            print('잘못된 메뉴 선택입니다.')
            return self.menu()

a = Tennis()





        






