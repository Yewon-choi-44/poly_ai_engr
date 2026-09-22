from classVarTest import Account
import random
import time

user1 = Account("user1", "월급", "1111", 2000000)

print("\n와! 월급날이다!٩( ᐖ )و\n")
time.sleep(1)
print(f" 입금 | 월급 |  {user1.total}원 | 잔액 | {user1.total}원 \n")
time.sleep(1)

while(True):
    if(user1.total<100000):
        time.sleep(1)
        print("\n 잔액이 부족합니다.\n (  ._.) <미친)")
        break
    else:
        user1.peogayo(random.randint(1000, 100000))
        time.sleep(0.7)
    