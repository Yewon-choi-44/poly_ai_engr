import pandas as pd
#시리즈 + 숫자 연산
'''
std1 = pd.Series({'kor':100, 'eng':80, 'math':90})
std2 = pd.Series({'eng':80, 'math':80, 'kor':90})

addition = std1.add(std1, fill_value=0)
print(addition)
fill_val=10

substraction = std1.substract(std2, fill_value=100)
multiplication = std1 * std2
#zero division 방지하기 위해서 입실론(굉장히 작은 값을 셋팅해서 사용)
#division = std1 / std2 #나누기 연산은 결과가 뭘까요?
division = std1.divide(std2, fill_value=0)

print()
print(std1/100)
print()
result = pd.Series([addition, multiplication, division],
                   index=['addition', 'multiplication', 'division'])

print(result)
print()'''

#10분정도 남았으니
#유인물에 6페이지 해보기


# 행/열 인덱스를 기준으로 정렬. 하는 명렁어.
# 일대일로 대응. 시키는 명령어? 그리고 연산. 하는 명령어.
# 원소값을 바꾸는. 명령어.
dict_data = {'c0':[1,2,3], 'c1':[5,4,6], 'c2':[7,8,9]}
df = pd.DataFrame(dict_data)
print("\n", df)


