total = 0 #초기 잔액은 0

def deposit(amount):
    global total
    total += amount
    print(f"입급 금액은 {amount}원 입니다. 현재 잔액은 {total}원 입니다.")
    
def withdraw(amount):
    global total
    if amount <= total:
        total -= amount
        print(f"출금 금액은 {amount}원 입니다. 현재 잔액은 {total}원 입니다.")
    else:
        print("출금액이 통장 잔고보다 큽니다. 처음 메뉴로 돌아갑니다.")
        
        
    
def check_balance():
    global total
    print(f"현재 잔액은 {total}입니다.")


