
standardPrice= {"쌀": 9900, "상추":1900, "고추":2900, "마늘":8900, "통닭": 5600, "햄": 6900, "치즈": 3900}

def getDiscountPrice(rate):
    dcPrice = {}
    for goods in standardPrice.keys():
        disPri = int(standardPrice[goods]*(1-(rate/100)))
        dcPrice[goods] = disPri
    return dcPrice

def printPrice(priceList):
    for goods in priceList.keys():
        print(goods, '\t:', standardPrice[goods], '원\t', inputData, '%DC ->', priceList[goods], '원')
        
print("-"*40)
print("-- 한빛마트 오늘의 할인 가격표 출력 시스템 --")
print("-"*40)

inputData = int(input("오늘의 할인율을 입력하세요. "))
discountPrice = getDiscountPrice(inputData)

printPrice(discountPrice)
print("-"*40)


'''
print("=" * 40)


text = "안녕하세요 여러분"
print(text)
print(type(text))
result = text.split()
print(result)
print(type(result))

text="apple, banana, grape"
result = text.split(",",2)
print(result)
'''

print("=" * 40)

text = "2026-03-29: 서버 오류가 발생했습니다."
result1=text.split(":")
text2 = "eslee@kopo.ac.kr"
result2=text2.split("@")
print(result1)
print(result2)

text3 = "첫번째 줄\n두번째 줄\n세번째 줄"
result3 = text3.split("\n")
print(result3)

text4 = "파이썬     프로그래밍    재미있어요"
result4= text4.split()
print(result4)



text5 = "5 + 3"
fomular=text.split()
print(fomular)

num1, operator, num2 = text5.split()

print(f"첫번째 숫자: {num1}")
print(f"연산자: {operator}")
print(f"두번째 숫자: {num2}")