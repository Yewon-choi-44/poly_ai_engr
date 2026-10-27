#1. 함수를 활용하여 사칙연산 기능을 구현하고, 사용자 입력을 받아 동작하는 계산기를 작성하고자 한다.
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들며, 사용자가 연산자와 숫자를 입력하면 결과를 출력한다.
# while 문을 사용하여 사용자가 'exit' 입력 시까지 반복 실행된다.
# split() 함수 사용.


#괄호 먼저 계산
#덧뺌곱낫 구분
#while문 exit
#split()으로 연산자와 숫자 구분


'''
def calculator():
    for i in range(len(cal)):
        if cal[i] == '+':
            
'''
def calculator(num1, num2):
    for i in range(len(cal)):
        if( cal[i]== "+") or  (cal[i]=="-") or (cal[i]=="*") or (cal[i]=="/"):
            num1 = float(cal[i-1])
            num2 = float(cal[i+1])
            
       
        
       #print(f"결과: {num1+num2}")
                     
       # elif cal[i]=="-":
       #     num1 = float(cal[i-1])
       #     num2 = float(cal[i+1])
       #     #print(f"결과: {num1-num2}")
                      
       # elif cal[i]== "*":
       #     num1 = float(cal[i-1])
       #     num2 = float(cal[i+1])
       #     #print(f"결과: {num1*num2}")
            
       # elif cal[i]=="/" :
       #     num1 = float(cal[i-1])
       #     num2 = float(cal[i+1])
       #     #print(f"결과: {num1/num2}")
       # else:
       #     break;  

while True: 
     cal = input("원하는 계산식을 입력하세요: ");
     cal=cal.split(" ");
     
     if cal == "exit":
         break;
     else:
         continue;
     
        
    
                
     calculator()