odd = 0;
even = 0;
i=1;

while (i < 101):
    if i % 2 == 0:
        even+=i;
    else:
        odd+=i;
        
print(f"1부터 100까지 숫자 중 짝수의 합은? {even}");
print(f"1부터 100까지 숫자 중 홀수의 합은? {odd}");