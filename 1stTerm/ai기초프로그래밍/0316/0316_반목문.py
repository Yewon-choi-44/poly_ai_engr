'''for num in range(1,10,2):
    print("num = ",num);
'''    
'''    
num = int(input('메일 발송 횟수를 입력하세요.'));
for num in range(1, num+1,1):
    print('메일 발송!');
'''   
'''    
for num in range(3,11,3):
    print('num=',num);
    if num %3 == 0:
        print(f'{num}은 3의 배수');
'''

'''for num in range(1, 10, 1):
    print(5,end='');
    print("*",end='');
    print(num, end='');
    print('=', end='');
    print(5*num);
    
    
    #print(f"{num} * i = {num*}");
'''


'''
num=0;
for i in range(1,10,1):
    num+=i;
print(f"1부터 10까지의 합: {num}");

num=0;
for i in range(2,10,2):
    num+=i;
print(f"1부터 10까지 짝수의 합: {num}");

num=0;
for i in range(1,10,2):
    num+=i;
print(f"1부터 10까지 홀수의 합: {num}")
'''


'''
sum=0;
even=0;
odd=0;

for i in range(1,11,1):
    sum+=i;
    if i%2==0:
        even+=i;
    else:
        odd+=i;
'''


'''
for i in range(10,0,-1):
    print(i);
'''


'''
num = 1;
while num <= 10:
    print('num:', num);
    num+=1;
'''

'''
num = 0;  
odd = 0;
even = 0;
sum_ = 0;
while num <= 10:
    if num%2 == 0:
        even += num;
        print(f"1부터 10까지 짝수의 합: {even}");
    elif num%2 == 1:
        odd += num;
    else:
        sum_ += num;
    
print(f"1부터 10까지 짝수의 합: {even}");
print(f"1부터 10까지 홀수의 합: {odd}");
print(f"1부터 10까지 합: {sum_}");
'''


'''
sum = 0;
even = 0;
odd = 0;
i=1;

while i <=10:
    sum+=i
    if i%2 ==0:
        even+=i
    else:
        odd+=i
    i+=1
    
print("1부터 10까지의 합",sum);
print("1부터 10까지의 짝수합",even);
print("1부터 10까지의 홀수합",odd);
'''


'''
for num1 in range(1,6):
    for num2 in range(num1):
        print("*",end="");
    print();
'''




