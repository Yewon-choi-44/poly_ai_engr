def calculator():
    for i in range(len(cal)):
         
        if cal[i]== "+" :
            num1 = float(cal[i-1])
            num2 = float(cal[i+1])
            
            print(f"결과: {num1+num2}")
                 
        elif cal[i]=="-":
            num1 = float(cal[i-1])
            num2 = float(cal[i+1])
            print(f"결과: {num1-num2}")
                  
        elif cal[i]== "*":
            num1 = float(cal[i-1])
            num2 = float(cal[i+1])
            print(f"결과: {num1*num2}")
        
        elif cal[i]=="/" :
            num1 = float(cal[i-1])
            num2 = float(cal[i+1])
            print(f"결과: {num1/num2}")
        else:
            break;  

while True: 
    cal = input("원하는 계산식을 입력하세요: ");
    
    if cal=="exit":
        break;
    else: 
        cal=cal.split(" ");
   
    calculator();
    