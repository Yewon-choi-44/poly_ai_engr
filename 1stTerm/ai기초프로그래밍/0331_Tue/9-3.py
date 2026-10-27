#3. 함수를 활용하여 랜덤 숫자 맞추기 게임을 작성하고자 한다.
# - random.randint(1,100)을 사용하여 1~100 사이의 랜덤 숫자를 생성한다.
# - 사용자에게 숫자를 입력받아 랜덤 숫자를 맞힐 때까지 반복한다.
# - 입력한 숫자가 랜덤 숫자보다 크거나 작으면 힌트를 제공한다.
# - 숫자를 맞히면 시도 횟수를 출력하고 종료한다.

import random

cnt = 0
luck = random.randint(1,100)
def gatcha(num):
    
    global cnt
        
    if num > luck:
        print("더 작은 숫자를 입력하세요!")
        cnt += 1
        
    elif num < luck:
        print("더 큰 숫자를 입력하세요!")
        cnt += 1
        
    else:
        print(f"정답입니다! {cnt}번만에 맞히셨습니다.")
        
    #num = int(input("숫자를 맞춰보세요: "))
    



while True:
    user = int(input("숫자를 맞춰보세요: "))
    gatcha(user)

    if user == luck:
        break;