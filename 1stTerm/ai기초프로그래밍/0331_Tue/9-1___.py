while True:

    cal = input("원하는 계산식을 입력하세요. (예: 5 + 3): ")
    
    if cal == "exit":
        break;
    
    num1= float(cal.split(" ")[0])
    num2= float(cal.split(" ")[2])
    oper = cal.split(" ")[1]
    
    
    def sum_():
        print(num1+num2)
    
    def sub():
        print(num1-num2)
    
    def mul():
        print(num1*num2)
    def div():
        print(num1/num2)
        
    
    def calculator():   
        if oper == "+":
            sum_()
        elif oper =="-":
            sub()
        elif oper =="*":
            mul()
        elif oper =="/":
            div()
            
    calculator();    