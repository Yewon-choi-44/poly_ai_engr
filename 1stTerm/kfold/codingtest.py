#3.

num_list = []
for i in range(3):
    num=input("정수를 입력하시오: ")
    num_list.append(num)




def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True