#12


#12

input1 = input("list1에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list1 = input1.split(" ")
input2 = input("list2에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list2 = input2.split(" ")
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(len(list2)):
    list2[i]=int(list2[i])
#소수: 1과 자기 자신만 인수로 가짐.

odd_1=[]
common_1=[]
odd_2=[]
common_2=[]

for i in range(len(list1)):
    if list1[i]%2 != 0:
        odd_1.append(list1[i])
    else: 
        continue

for i in range(len(list2)):
    if list2[i]%2 != 0:
        odd_2.append(list2[i])
    else: 
        continue

print(odd_1)
print(odd_2)






'''
input1 = input("list1에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list1 = input1.split(" ")
input2 = input("list2에 넣을 정수를 입력하시오. (각 수는 공백으로 구분하시오.): ")
list2 = input2.split(" ")
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(len(list2)):
    list2[i]=int(list2[i])
#소수: 1과 자기 자신만 인수로 가짐.

print(list1)
print(list2)






common =[]

'''




'''



if len(list1)>len(list2):
    for i in range(len(list1)):
        if list1[i] in list2:
            common.append(list2)
        else:
            continue
    print(common)

elif len(list1)<len(list2):
    for i in range(len(list2)):
        if list2[i] in list1:
            common.append(list1)
        else:
            continue
    print(common)

else:
    for i in range(len(list2)):
            if list2[i] in list1:
                common.append(list1)
            else:
                continue
    print(common)


'''

#def find_common_prime(list1, list2):