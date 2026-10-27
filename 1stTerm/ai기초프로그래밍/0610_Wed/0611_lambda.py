'''
def adult_func(n):
    if n >= 19:
        return True
    else:
        return False
    
    
ages = [34, 39, 20, 18, 13, 54]
print('성년 리스트: ')
for a in filter(adult_func, ages):
    print(a, end=' ')
'''
#########################################
'''
def minus_func(n):
    if n<0:
        return True
    else:
        return False
    
n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list=[]
for n in filter(lambda x: x<0, n_list):
    minus_list.append(n)
print('음수 리스트: ', minus_list)
'''
#########################################
'''
# def square(x):
#     return x** 2

a = [1, 2, 3, 4, 5, 6, 7]

square_a = list(map(lambda x: x<5, a))
print(square_a)
'''
##########################################

# 리스트 축약 
    # 기본 문법:
        # [표현식 for 변수 in Iterable 자료형] 
        # e.g.) squares = [x**2 for x in range(1, 6)]
        #       print(squares) # 출력:[1, 4, 9, 16, 25]
    
    # 조건이 있는 문법:
        # [표현식 for 변수 in Iterable 자료형 if 조건 표현식]
        # e.g.) result = [x**2 for x in range(1, 6) if x % 2 == 0]
        #       print(result) # 출력: [4, 16]
        
squares = [x**2 for x in range(1, 6)]
print(squares) # 출력:[1, 4, 9, 16, 25]

result = [x**2 for x in range(1, 6) if x % 2 == 0]
print(result) # 출력: [4, 16]



a = [1, 2, 3, 4, 5, 6, 7]
b1 = list(map(lambda x: x**2, a)) # 리스트의 각 요소에 대하여 람다 함수 적용
print(b1)
b2 = [x**2 for x in a] # 리스트의 각 요소에 대하여 x**2 적용
print(b2)
b3 = [x**2 for x in range(1,8)]
print(b3)



###########################################
# if 조건식을 이용한 필터링:
    
ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print(f'성년 리스트 : {adult_ages}')
print(f"성년 리스트 : {[x for x  in ages if x >= 19]}")
print(f"미성년 리스트 : {[x for x  in ages if x <= 19]}")

###########################################
n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = list(filter(lambda x: x < 0, n_list))
plus_list = [x for x in n_list if x > 0]
print(f'음수 리스트 : {minus_list}')
print(f'양수 리스트: {plus_list}')
############################################
# 리스트 축약 표현과 if 조건식을 이용한 필터링

# 빈 공백("")을 삭제 후 출력하시오.
words = ["apple", "", "banana", "", "cherry"]
words = [x for x in words if x!=""]
print(words)










