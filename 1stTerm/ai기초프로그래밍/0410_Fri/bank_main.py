import bank_module as bank

while True:    
    sel = int(input("\n[은행 계좌 시스템 ]\n 1. 입금 \t 2. 출금 \t 3. 잔액 조회 \t 4. 종료 \n"))
    print()
    if sel == 1:
        inputData = int(input("입금할 금액: "))
        bank.deposit(inputData)
        print()
        continue
        
    elif sel == 2:
        inputData = int(input("출금할 금액: "))
        bank.withdraw(inputData)
        print()
        continue
        
    elif sel == 3:
        bank.check_balance()
        print()
        continue
        
    elif sel == 4:
        print("시스템을 종료합니다.")
        print()
        break
    else:
        print("잘못 누르셨습니다. 다시 하시오")
        print()
        continue
    
