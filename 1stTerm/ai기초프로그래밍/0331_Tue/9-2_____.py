total = 0 #초기 잔액은 0

def deposit(cash):
    global total
    total += cash
    print(f"입급 금액은 {cash}원 입니다. 현재 잔액은 {total}원 입니다.")
    
def withdraw(cash):
    global total
    if cash <= total:
        total -= cash
        print(f"출금 금액은 {cash}원 입니다. 현재 잔액은 {total}원 입니다.")
    else:
        print("출금액이 통장 잔고보다 큽니다. 처음 메뉴로 돌아갑니다.")
        
        
    
def check_balance():
    global total
    print(f"현재 잔액은 {total}입니다.")


while True:
    sel = int(input("\n[은행 계좌 시스템 ]\n 1. 입금 \t 2. 출금 \t 3. 잔액 조회 \t 4. 종료 \n"))
    print()
    
    if sel == 1:
        inputData = int(input("입금할 금액: "))
        deposit(inputData)
        print()
        
    elif sel == 2:
        inputData = int(input("출금할 금액: "))
        withdraw(inputData)
        print()
        
    elif sel == 3:
        check_balance()
        print()
        
    elif sel == 4:
        print("시스템을 종료합니다.")
        print()
        break
    else:
        print("잘못 누르셨습니다. 다시 하시오")
        print()
        continue
    