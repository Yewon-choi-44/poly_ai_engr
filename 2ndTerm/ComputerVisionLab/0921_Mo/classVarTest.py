class Account:
    cntAccount = 0
    uniqAccountNum = 10000
    total = 0

    def __init__(self, name, alias, passwd, total):
        Account.cntAccount += 1
        Account.uniqAccountNum +=1 
        self.name = name
        self.alias = alias
        self.passwd = passwd
        self.numUniqAccount = Account.uniqAccountNum
        self.total = total

    def income(self, money):
        Account.total += money
        self.total += money

    def withdraw(self, money):
        Account.total -= money
        self.total -= money

    def peogayo(self, money):
        
        Account.total -= money
        self.total -= money
        print(f" 출금 | 퍼가요~♡ | -{money}원 | {self.total}원")
        return self.total

# user1 = Account("user1", "용돈", "1234")
# user2 = Account("user2", "월급", "0000")
# user3 = Account("user5", "월급", "5678")
# user4 = Account("user3", "삥", "9999")

# fing = int(input("얼마를 뜯으시겠습니까? : "))

# user1.income(1000000)
# user2.income(20000000)
# user3.income(30000000)
# user4.withdraw(fing)

# # print(f"{Account.cntAccount}")
# # print(f"{Account.uniqAccountNum}")
# # print(f"{Account.total}")
# # print(f"{Account.withdraw}")

# # print(f"{user1.total}")
# # print(f"{user2.total}")
# # print(f"{user3.total}")
# print(f"{user3.name}이(가) {user4.name}에게 {user4.alias}을 {fing}원 뜯었습니다.")

# # 회사 , 신입사원 등을 예시로 클래스 변수 관련 코드 하나 작성해보기.
# # 위 코드에서 여러가지 테스트 해보기 등등...