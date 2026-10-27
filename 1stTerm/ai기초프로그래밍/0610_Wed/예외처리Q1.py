# # 1. [1,2,3,4,5]의 다섯 개의 요소를 가진 리스트 a가 있을 때 
# 다음과 같이 사용자로부터 정수를 입력받은 후 
# 이에 해당하는 인덱스를 출력하도록 프로그램을 작성하시오. q1.py
# - 단, 정수가 아닌 값이 예를 들어 '삼'이 입력되면 try-except 문 사용하여 에러 메시지까지 출력.


a = [1, 2, 3, 4, 5]
print(a)

try:
    num = int(input("a의 원소를 하나 선택하시오: "))
    for i in num:
        
        if num == i:
            print(f"{num}은 {i}번째 원소입니다.")
        else:
            print(f"{num}은 a의 원소가 아닙니다.")
except ValueError as e:
    print()
    print("입력값이 정수나 실수가 아님", e)
    print()