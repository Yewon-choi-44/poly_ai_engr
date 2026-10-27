'''input1 = input("list1에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list1 = input1.split(" ")
input2 = input("list2에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list2 = input2.split(" ")
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(len(list2)):
    list2[i]=int(list2[i])



if len
for i in range():
'''

input1 = input("list1에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list1 = list(map(int, input1.split()))
input2 = input("list2에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list2 = list(map(int, input2.split()))
print(list1, list2)

common = []
if len(list1) > len(list2):
    len_list=len(list1)
    for i in range(len_list):
        if list1[i] in list2:
            common.append(list1[i])
elif len(list1) <len(list2):
    len_list=len(list2)
    for i in range(len_list):
        if list2[i] in list1:
            common.append(list2[i])
else: 
    len_list=len(list1)
    for i in range(len_list):
        if list1[i] in list2:
            common.append(list1[i])
print(common)



# for i in range(len(common)):    
#     cnt=0
#     if common[i]%i==0:
#         cnt+=1

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

final_primes = []
for i in range(len(common)):
    is_prime(common[i])
    if is_prime(common[i]):
        final_primes.append(common[i])
    

print(final_primes)