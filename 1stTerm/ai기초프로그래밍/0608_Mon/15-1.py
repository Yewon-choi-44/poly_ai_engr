# 1. 문자열 리스트에서 길이가 5 이상인 단어만 대문자로 변환하여 출력하시오. 
# words = ['apple', 'pear', 'banana', 'kiwi','pineapple','grape']

# 필터함수, 리스트 함수, 람다함수 등을 활용하시오.
# 길이가 5 이 상인 단어만 필터링하고, 해당 단어들을 대문자로 변환하시오.

words = ['apple', 'pear', 'banana', 'kiwi','pineapple','grape']

'''
FilterWords = [x for x in words if len(x)>=5]
print("FilterWords",FilterWords)
UpperFilterWords = [x.upper() for x in FilterWords]
print("길이 5 이상 단어의 대문자 변환 결과",UpperFilterWords)
'''

FilterWords2 = list(filter(lambda x: len(x)>=5, words))
UpperFilterWords2 = [x.upper() for x in FilterWords2]
print(f"길이 5 이상인 단어의 대문자 변환 결과: {UpperFilterWords2}")



# ##############################################################
# 2. (이름, 점수)로 구성된 튜플 리스트에서 60점 이상인 학생의 이름만 리스트로 출력하시오.
# [구현 조건]
#     - 이름과 점수로 구성된 튜플의 리스트가 주어진다.
#       students = [('Alice', 85), ('Bob', 58), ('Charlie', 90), ('David', 45), ('Eve', 70)]
#     - 리스트 함축을 사용하시오.

students = [('Alice', 85), ('Bob', 58), ('Charlie', 90), ('David', 45), ('Eve', 70)]
