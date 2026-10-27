class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount}원 입금 완료!")
        return self.balance
       
    def withdraw(self, amount): #출금
        if(self.balance>=amount):
            self.balance = self.balance-amount
            print(f"{amount}원 출금 완료!")
            return self.balance
        else:
            print("잔고가 부족합니다.")
        
    def check_balance(self): #잔고
      
        print(f"현재 잔고: {self.balance}")    
        return self.balance
    
    def account_info(self): #싹다 찍기
        print(f"계좌번호: {self.account_number}")
        print(f"고객 이름: {self.customer_name}")
        print(f"현재 잔고: {self.balance}")
        
account = BankAccount("123-456", "홍길동", 10000)
account.account_info()
account.deposit(5000)
account.withdraw(3000)
account.check_balance()