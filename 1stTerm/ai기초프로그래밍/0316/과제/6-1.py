#for문을 이용하여 1~100까지 짝수합과 홀수합 출력

even=0;
odd=0;
for i in range(1,101):
    if i%2==0:
       even+=i;
    else:
        odd+=i;
print(f"1부터 100까지 숫자 중 짝수의 합은?: {even}");
print(f"1부터 100까지 숫자 중 홀수의 합은?: {odd}");