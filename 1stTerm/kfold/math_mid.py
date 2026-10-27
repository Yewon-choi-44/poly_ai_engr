'''def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    # 1과 자기 자신을 제외한 나머지 모든 수(2~n-1) 중 하나라도
    # 나누어 떨어지면 소수가 아님.
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution_8():  # 함수에 반드시 인자가 있을 필요는 없다. return값이 꼭 있어야하는 것도 아니다...전역변수를 건드린다면 구태여 return을 사용하지 않아도 된다.
    # 전역변수는 반드시 사용해야하는 것이 아니라면 지양하는 것이 좋다. (어떤 함수라도 그 변수에 접근할 수 있기 때문에...)
    n = 15
    # 한글로 명시되어 있는 작업 지시서를 보고
    # 코드로 만들어 낼 수 있는지를 확인.
    # 을 보기 위해 문제를 내셨다.

    exp_num_list = []
    # 1. 1~15 숫자 중에 소수를 판단해야 함.
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    temp_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    # 2. 르장드르 공식 적용
    for p in primes:
        temp_n = n
        sum_exp = 0
        while temp_n >= p:
            sum_exp += temp_n // p
            temp_n //= p
        exp_num_list.append(sum_exp)
    return exp_num_list, (exp_num_list)

#print(exp_num_list)
'''

'''
from sympy.ntheory import factorint
print(factorint(67982341)) # 결과: {2: 2, 3: 1} -> 2^2 * 3^1
'''

'''
def my_max(input_list):
    max=0
    for val in input_list:
        if val > max:
            max=val
        else:
            continue
        return max

def is_prime(num):
    if num < 2:
         return False
    if num == 2:
        return True

    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def solution_8(n):
    n=67982341
    exp_num_list = []
    primes = [i for i in range(2, n+1) if is_prime(i)]
    temp_list = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)

    #2. 르장드르 공식 적용
        for p in primes:
            temp_n = n
            sum_exp = 0
            while temp_n >= p:
                sum_exp += temp_n // p
                temp_n //= p
            exp_num_list.append(sum_exp)
        return exp_num_list
    print(exp_num_list)

solution_8(67982341)

'''

def get_largest_prime_factor(n):
    i = 2
    # n의 제곱근까지만 반복하여 효율성 증가
    while i * i <= n:
        if n % i == 0:
            n //= i # 소인수로 나누어 몫 갱신
        else:
            i += 1
    return n # 남은 n이 가장 큰 소인수

# 예시: 600851475143의 가장 큰 소인수 구하기
number = 67982341
print(get_largest_prime_factor(number)) # 결과: 6857

'''
def solution_7(input_data1, input_data2):
        #[2, 2, ,2, 3, 4, 5, 6, 7]
        #[2, 3, 4, 6, 9]
        # 2중 for문으로 동일한 값을 먼저 저장

    common_list = set(input_data1) & set(input_data2) #리스트의 내장함수 중 set을 쓰면 중복을 배제해준다.
    result = []
    for num in common_list:
        if is_prime(num):
            result.append(num)
    return result
'''






'''def cost_function(W, X, y):
    """
    W: 가중치(Weight)
    X: 입력 데이터
    y: 실제값
    """
    m = len(y)  # 데이터 개수
    predictions = X * W  # 가설 함수: h(x) = Wx (편향 b 생략한 단순 모델)

    # MSE Cost = (1/m) * sum((pred - y)^2)
    cost = (1 / m) * np.sum(np.square(predictions - y))
    return cost
'''

'''
import numpy as np

def cos_sim(a, b):
    # np.dot(a, b): 내적 (Dot Product)
    # np.linalg.norm(a): 벡터의 크기 (Norm)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 예시 벡터
vec1 = np.array([0.2, 0.4, 0.02, 0.1, 0.9, 0.8])
vec2 = np.array([0.1, 0.2, 0.01, 0.05, 0.45, 0.4])

similarity = cos_sim(vec1, vec2)
print(np.dot(vec1, vec2))
print(f"코사인 유사도: {similarity}")

'''
'''
import math
import numpy as np

def cosine_similarity(v1, v2):
    # 1. 내적 계산 (Dot Product)
    dot_product = sum(a * b for a, b in zip(v1, v2))

    # 2. 각 벡터의 크기 계산 (Norm) - math.sqrt 활용
    norm_v1 = math.sqrt(sum(a ** 2 for a in v1))
    norm_v2 = math.sqrt(sum(b ** 2 for b in v2))

    # 3. 분모가 0이 되는 경우 방지
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0

    # 4. 코사인 유사도 반환
    return dot_product / (norm_v1 * norm_v2)


# 예시 벡터
vec1 = np.array([0.2, 0.4, 0.02, 0.1, 0.9, 0.8])
vec2 = np.array([0.0, 0.1, 0.0, 0.0, 0.2, 0.1])

similarity = cosine_similarity(vec1, vec2)
dot=sum(a * b for a, b in zip(vec1, vec2))
print(dot)
print(f"코사인 유사도: {similarity:.4f}")  # 0.9746
'''