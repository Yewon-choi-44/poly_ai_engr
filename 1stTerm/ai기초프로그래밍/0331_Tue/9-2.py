# 2. 함수를 활용하여 은행 계좌 관리 시스템을 작성하고자 한다.
# - 은행 계좌의 입금, 출금, 잔액 조회 기능을 함수로 구현한다.
# - deposit(금액): 입금 함수(잔액 증가)
# - withdraw(금액): 출금 함수(잔액 감소)
# - check_balance(): 잔액 조회 함수
# - while문을 사용해 사용자가 종료할 때까지 반복 실행한다.
# 매개변수....

total = 0 # 초기 total = 0

def deposit(total):
    total += cash
    print(f"{cash}원이 입금되었습니다. 현재 잔액:{total}")
    
def withdraw(total):
    #cash = int(input("출금할 금액: "))
    # 출금 금액이 현재 통장 잔액보다 크면 안된다
    
    if total >= cash :
        total-=cash
        print(f"{cash}원이 출금되었습니다. 현재 잔액: {total}")
        
    else:
        print("마이너스 통장은 안된다 파산하고 싶나?ㄴ")
            
    
    
def check_balance():
    print(f"현재 잔액: {total}")
    
'''def calculator():
    if sel == 1:
        #cash=int(input("입금할 금액: "))
        deposit();
    elif sel==2:
        #cash=int(input("출금할 금액: "))
        withdraw();
    elif sel ==3:
        check_balance();
    elif sel ==4:
     print("시스템을 종료합니다.")
    else:
        print("그딴 메뉴는 없습니다. 다시 고르시오.")
        '''
    
while(True):
    
    print("[ 은행 계좌 시스템 ]\n")
    sel = int(input("1. 입금 \t 2. 출금 \t 3. 잔액 조회 \t 4. 종료\n"))
    
    
    if sel == 1:
        cash=int(input("입금할 금액: "))
        deposit(total);
    elif sel==2:
        cash=int(input("출금할 금액: "))
        withdraw(total);
    elif sel ==3:
        check_balance();
    elif sel ==4:
     print("시스템을 종료합니다.")
    else:
        print("그딴 메뉴는 없습니다. 다시 고르시오.")
    
    


#cash=int(input("입금할 금액: "))


        
    
    

    
    
  