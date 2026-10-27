def greet():
    print("안녕하세요.")
    print("반갑습니다.")
    print("저는 홍길동입니다.")
    
    
greet();
greet();

print("="*40)

def startTemperatureSensor():
    print("온도센서 작동을 시작한다.")
def stopTemperatureSensor():
    print("온도센서 작동을 중지한다.")
    
'''startTemperatureSensor()
stopTemperatureSensor()


print("="*40)


def converUnit():
    print(lengthCm, 'cm= ', lengthCm*0.393701, 'inch');
lengthCm = float(input("길이를 입력하세요.(cm) "))
converUnit();



print("="*40)

def calculateDistance():
    print("이동 거리는", hourData*speedData, 'km 입니다.')
    
hourData = float(input("이동 시간을 입력하세요. "))
speedData = float(input("이동 속도를 입력하세요. "))
calculateDistance();


print("="*40)



def add():
    print("덧셈 결과: ", inputNumber1 + inputNumber2)
def sub():
    print("뺄셈 결과: ", inputNumber1 - inputNumber2)
def mul():
    print("곱셈 결과: ", inputNumber1 * inputNumber2)
def div():
    print("나눗셈 결과: ", inputNumber1 / inputNumber2)
    
def calculator():
    if(selectOperator == 1):
        add()
    elif(selectOperator == 2):
        sub()
    elif(selectOperator == 3):
        mul()
    elif(selectOperator == 4):
        div()
        
inputNumber1 = float(input("숫자를 입력하세요. "))
selectOperator = int (input("연산자를 선택하세요. 1.덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈 "))
inputNumber2 = float(input("숫자를 입력하세요. "))

calculator();


print("="*40)
'''
'''
#연ㄴ습문제2
sae = int(input("새우깡 구매 개수: "));
vivi = int(input("비비빅 구매 개수: "));
choco = int(input("초코파이 구매 개수: "));
mat = int(input("맛동산 구매 개수: "));
sum_ = 0

print("="*30)

def print_recipt():
    print(f"새우깡 구매 개수: {1200*sae}")
    print(f"비비빅 구매 개수: {400*vivi} ")
    print(f"초코파이 구매 개수: {500*choco} ")
    print(f"맛동산 구매 개수: {1500*mat}")
    print("="*30)
    print(f"총 구매 금액: {1200*sae+400*vivi+500*choco+1500*mat}");
    
print_recipt();'''


'''
num = 10;
def fun1():
    global num
    num=30
    print("num: ", num)

print('num: ', num)
fun1()
print('num : ', num)



'''
'''

flag = True 
totalVisitor =0;

def countVisitor():
    global totalVisitor
    totalVisitor +=1
    
    
while flag:
    inputData = int(input("1. 웹사이트 방문, 2. 종료 "))
    
    if inputData == 1:
        countVisitor()
        print("누적 방문 횟수: ", totalVisitor)
    else:
        flag = False
        
        
        
        
def greet(name):
    print(name, "씨, 안녕하세요.");
    
    
greet("홍길동")
greet("박찬호")
greet("박지성");




def printAverageScore(*scores):
    print(type(scores))
    
    
    totalScore = 0
    cnt = len(scores);
    
    for score in scores:
        totalScore += score
    print("총점: ", totalScore, '점')
    print("평점: ", totalScore / cnt, "점")
    print("-----------------------------------------")
    
printAverageScore(80, 90, 70)
printAverageScore(90, 85, 90, 100)
printAverageScore(95, 80, 100, 95, 85)






def addFunction(n1, n2):
    sum = n1 +n2
    avg = sum/2;
    return sum, avg;

result = addFunction(10, 20)
print(result)
'''

'''
def divFunction(n1, n2):
    def divOperator(num1, num2):
        return num1/num2
    
    if n2 != 0 :
        result = divOperator(n1,n2)
    elif n2 == 0:
        result = '0으로 나눌 수 없습니다.'
    return result

print(divFunction(10,0))
print(divFunction(10,2))
'''






def factorialFun(num):
    if num == 1:
        return 1
    else :
        return num * factorialFun(num - 1)
    
inputData = int(input("0보다 큰 숫자를 입력하세요. "))
result = factorialFun(inputData)
print(inputData, "팩토리얼은 ", result, "입니다.")