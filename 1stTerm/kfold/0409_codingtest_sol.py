from openpyxl.styles.builtins import total
from sympy import fibonacci

if __name__ == "__main__":

    #1. 변수를 지정할 수 있고, 출력 기초 출력 확인
    # 변수명으로 str <-- 지양해주세요.
    str_val  ="Hello World"
    #예약어는 사용x
    print(str_val)



    #2. 입력을 받을 수 있는지
    # input 메서드로 반환되는 자료형은 문자열
    # 연산을 할 경우 반드시 형변환 해주어야 함
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # 연산자 중에 몫 연산자 알고 있는지.
    # 자료형 중 튜플에 대해 이해하고 있는지.
    # 나누기를 할 경우, 소수점 발생시 .... // 사용할 수 잇는지...?
    result = (num1 + num2, num1 * num2, num1//num2)
    print(num1)
    print(num2)


    #3. 빈 리스트 만들고 append 메서드를 아는지
    # 입력을 세 번 받을건지... ==> 반복문 사용할 건지...

    result = []
    for i in range(3):
        num = int(input("Enter a number: "))
        result.append(num)


    #4. Slicing 가능 여부
    text = "pythonProgramming"
    print(text[:]) #변수를 무조건 지정하는 것을 연습.


    #5. 딕셔너리 자료형으로부터 특정 키에 해당하는 값을 가지고 올 수 있는지
    # dict = {key:value , key1 : value1}
    # value ==> dict['key']
    # 나이 + 1 --> 형 변환 하면 되는데

    info = {'name':'Alice', 'age': '20', 'city': 'Daegu'}
    name = info['name']
    age = info['age']

    #문자열 내장 함수 사용 ( <-- 찍어보고 메서드 좀 보라구요...)
    print(f'{name} -> {name.lower()}')
    print(f'{age} -> {int(age) + 1}')


    # 6. 문자열 분리, 슬라이싱, 등등...
    import random #최상단에 위치하는 게 좋으나 풀이 보기 좋게 여기 적겠음.
    def solution_1(input_data):
        #split 메서드는 특정 문자를 기준으로 짤라 리스트로 반환
        split_data = input_str.split("-")
        #split_data => ['2026', '04', '09']
        year = int(split_data[0][2:])
        month = int(split_data[1])
        day = int(split_data[2])
        return year, month, day


    #7.
    def solution_2(input_data):
        # 함수의 반환이 홀수들의 모음
        # 홀수만 담을 수 있는 공간이 필요함
        odd_list = []
        for num in input_data:
            if num % 2 == 0:
                odd_list.append(num)
        return odd_list

        # 제일 formal한 형태는 아래가 맞다.
        # for idx in range(len(input_data)):
        #    if input_data[idx] % 2 == 0:
        #        odd_list.append(input_data[idx])
        #    return odd_list



        # 종종 정해져 있는 반복 숫자이기 때문에 하드코딩 ==> 지양 (하드코딩을 하지 않을 수 있는 방법이 있다면 그쪽으로.)
        # for num in range(len(input_data)):
        # for num in input_data:

        # for num in range(10):
        # loop = len(input_data)
        # for num in range(loop):

        #if input_data[0] == '0':
        #    odd_list.append(input_data[1])
        # even_list = [] 치지 말라셧다. 코드가 정말 힘들면 이렇게라도 해야한다 하셧다.
        # 이렇게 10개를 쓰면 문제를 풀 수 있다. -> for문의 필요성을 느낄 수 있어야 한다.

    input_str = '2026-04-09'
    result = solution_1(input_str)
    print(f"today is {result[0]}, {result[1]}, {result[2]}")
    random.seed(100)
    input_list=[random.randint(1, 3000) for i in range(10)]



 #8.
    def solution_3(fruits, price, fruit_counts):
        total = 0
        fruit_dic = dict(zip(fruits, price))

        for key in fruit_dic.keys():
            total += fruit_dic[key] * fruit_counts[key]
        return total


    fruits = ("apple", "banana", "cherry")
    price = (4000,3000,5000)
    # example
    fruit_counts = {}
    # fruit_counts = {"apple":3, "banana":1 ,"cherry":2}
    # zip_dict = {"apple" :4000, "banana": 3000, "cherry":5000}
    for fruit in fruits:
        count = int(input(f'{fruit}: '))
        fruit_counts[fruit] = count

 #9. 주어진 리스트에서 양수, 음수를 구분할 수 있나?
    # 리스트 중첩으로 처리할 수 있고,
    # lanbda --> 처리할 수 있나?
    # input_Data : 문제에서 주어진 리스트
    def solution_4(input_data):
        neg_sum = 0 # +=
        pos_sum = 0 # list로 정의를 하면 append.
        for v in input_data:
            if v < 0:
                neg_sum += v
            elif v > 0 :
                pos_sum += v
        # 리스트 컨프리헨션...
        neg_sum = sum([for v in input_data if v < 0])
         = sum([v for v in input_data if v > 0])
        return abs(neg_sum) - abs()

        # filter <-- 안 배웠으니 나중에 해보세요....
        pos_sum = sum(list(filter ( lambda x: x > 0 , input_data )))
        neg_sum = sum(list(filter ( lambda x: x < 0 , input_data )))
        return abs(neg_sum) - abs(pos_sum)


    #10.
    # dictonary type --> 키에 해당하는 값을 읽을 수 있는지
    # 키가 없는 상태에서 += 와 같은 연산이 불가...
    def solution_5(input_data):
        char_count = {}
        for s in input_data: #다른 언어에서는 char이 자료형이기 때문에 되도록 변수명으로는 피한다. 파이썬에서는 쓸 수는 있다.
            if s.isalpha(): #알파벳 여부 체크(, <- 아님)
                if s in char_count: #이 if문이 없으면 아무 것도 없는 곳에다 값을 매핑을 하려는 것이기 때문에...
                    # 있는지를 체크하지 않는거는
                    # Null + 1 이라. 반드시 error가 발생했을 거다...
                    # 이 연산이 불가능한지 확인하는가.... 그걸 보려는 문제...였다...
                    char_count[s] += 1
                else:
                    char_count[s] = 1

    #11.
    # 최댓값과 최댓값의 인덱스를 반환하는 함수
    # 정렬을 하라고 하는 게 아님.
    # v[i] > v[i+1]:
    # 변수를 하나 두고, 이 변수가 리스트 전체를 체크하면서 더 큰 값이 있는지만 확인

    def solution_6(input_data):

        rtn_value = [float('-inf'),-1] # value, index  반환하기 위해 리스트로
        #max(input_data), min(input_data) <이게 제일 빠르긴 하지만 for문과 enumerate를 아는지 알기 위해 낸 문제다...
        for idx, num in enumerate(input_data):
            if num >= rtn_value[0]:
                rtn_value[0] = num
                rtn_value[1] = idx
        return tuple(rtn_value)


    #12.
    #소수: 약수가 1과 자기 자신인 수
    # 2, 3, 5, 7, 11, 13...
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        # 1과 자기 자신을 제외한 나머지 모든 수(2~n-1) 중 하나라도
        # 나누어 떨어지면 소수가 아님.
        for i in range(2, num):
            if num%i == 0:
                return False
        return True


#13
    def solution_7(input_data1, input_data2):
        #[2, 2, ,2, 3, 4, 5, 6, 7]
        #[2, 3, 4, 6, 9]
        # 2중 for문으로 동일한 값을 먼저 저장
        common_data = []
        for i in input_data1:
            if i in input_data2:
                if i == j:
                    common_data.append(i)
        #common_data = [2, 2, 2...]
        #set이라는 걸! 써보셨으면 좋겠다!
        # set + bit 연산자...
        # 중복 여부까지 파악해야 한다면...
        common_list = set(input_data1) & set(input_data2) #리스트의 내장함수 중 set을 쓰면 중복을 배제해준다.
        result = []
        for num in common_list:
            if is_prime(num):
                result.append(num)
        return result

    #13.
    def solution_8(): #함수에 반드시 인자가 있을 필요는 없다. return값이 꼭 있어야하는 것도 아니다...전역변수를 건드린다면 구태여 return을 사용하지 않아도 된다.
        # 전역변수는 반드시 사용해야하는 것이 아니라면 지양하는 것이 좋다. (어떤 함수라도 그 변수에 접근할 수 있기 때문에...)
        n = 15
        # 한글로 명시되어 있는 작업 지시서를 보고
        # 코드로 만들어 낼 수 있는지를 확인.
        # 을 보기 위해 문제를 내셨다.

        exp_num_list = []
        # 1. 1~15 숫자 중에 소수를 판단해야 함.
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
        return exp_num_list, (exp_num_list)

    #14. 피보나치 수열

    def solution_9(n):
        #초기값
        fibonacci = [0,1]

        if n == 0:
            return[0]
        elif n == 1:
            return[0, 1]

        for i in range(2, n+1):
            next_fibo = fibonacci[i-1] + fibonacci[i-2]
            fibonacci.append(next_fibo)

        return fibonacci



    #15.
    #계산복잡도: 0(N) --> example: 이중 for
    def solution_10(in_list, M, K):
        result = 0
        # solution6: 제일 큰 값 및 큰 값에 해당하는 인뎃ㄱ스
        # 좋은 방법은 아니라 하심....
        max_val1, max_idx1 = solution_6(in_list)
        in_list.remove(max_val1) #
        max_val2, max_idx2 = solution_6(in_list)
        # 삭제하지 말고 for문 돌면서 다음 max값 ㅊ자아볼 것...

        count = 0
        for i in range(M):
            if count != K:
                result += max_val1
                count += 1
            else:
                result += max_val2
                # 이렇게 해야 반복문에서 제일 큰 값을 K번만큼 더할 수 있음...
                count = 0
        return result

    def solution_11(in_list,M,K):
        result = 0
        # 오름차순으로 정렬. (reverse --> 내림차순 정렬.)
        in_list.sort(reverse=True)
        max_num1 = in_list[0]
        max_num2 = in_list[1]

        #maxval1=6, maxval2=5
        #6665 6665 66
        total_loop = M // (K+1)
        add_rest = M % (K+1)
        mul_val = (max_num1 * K) + max_num2 #6665
        result = (mul_val * total_loop) + (max_num1 * add_rest)
        # 연산의 우선순위로 인해 결과가 다르게 도출될 수 있어
        # 괄호를 항상 넣는 습관을 가집시다.
        # 사칙연산의 우선순위는 다들 잘 알고 있음
        # num ** (1/2)
        # (num ** 1)/2 #사칙연산 우선순위 때문에 괄호를 치는 습관을 들일 것
        return result



import time
if __name__ == '__main__':
    print("a")


    in_list = [2,4,5,4,6]

    start_time.time()
    print(solution_10(in_list, M:900000000, K:3))
    end = time.time()

