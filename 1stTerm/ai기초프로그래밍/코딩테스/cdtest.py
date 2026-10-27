#3. 
'''
num_list = []
# for i in range(3):
#     num=int(input("정수를 입력하시오: "))
#     num_list.append(num)

num = input("정수를 3개를 입력하시오: ")
num= num.split(" ")

for i in range(len(num)):
    num_list.append(int(num[i]))

print(num_list)



#4

py = "PythonProgramming"

py_1= py[:6]
py_2=py[6:]

print(f"First String is {py_1}")
print(f"Second String is {py_2}")

'''

'''
#5
dict = {'name': 'Alice', 'age':'20', 'city':'Daegu'}
print(f"{dict['name']} -> {dict['name'].lower()} \n")
print(f"{dict['age']} -> {int(dict['age'])+1}")


#6.
input_str= input("날짜를 입력하시오(예: 2026-04-06): ")
year, month, date = input_str.split("-")


    print(f"오늘은 {year[2:4]}년 {month[]}월 {date[-1]}입니다.")

'''






'''


letters='python'
print(letters[0], letters[2])
print(letters[0:3])


license_plate = "24가 2210"
print(license_plate[-4:])


'''




input_str = "Hello, World!!"
print(input_str.isalpha())