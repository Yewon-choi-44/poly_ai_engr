#사칙연산을 계산하는 프로그램
while(True):
    print("== 메뉴 ==");
    print("1. 덧셈 \n2. 뺄셈 \n3. 곱셈\n4. 나눗셈");
    print("="*10);
    cal=int(input("선택: "));
    
    num1 = int(input("\n첫 번째 수 입력: "));
    num2 = int(input("두 번째 수 입력: "));
    
    if cal == 1:
        print(f"{num1} + {num2} = {num1+num2}");
        break;
    elif cal == 2:
        print(f"{num1} - {num2} = {num1-num2}");
        break;
    elif cal == 3:
        print(f"{num1} x {num2} = {num1*num2}");
        break;
    elif (cal == 4) and ((num1 != 0) and (num2 != 0)):
        print(f"{num1} / {num2} = {num1/num2}");
        break;
    elif (num1 == 0) or (num2==0):
        print("나눌 수 없음.");
        break;
    else: 
        print("\n보기를 다시 골라라.\n");
        continue;
        