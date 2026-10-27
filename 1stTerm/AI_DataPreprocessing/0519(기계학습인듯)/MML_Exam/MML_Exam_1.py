# 1. 리스트 내장 함수 중 pop() 함수를 구현
    # pop() 함수에 인자를 넣지 않고 실행하면
        # 리스트의 제일 마지막 요소를 반환하고
        # 리스트의 마지막 원소를 삭제한다.
    # pop(1) 과 같이 인자에 인덱스를 넣으면
        # 인덱슨에 해당하는 값을 리스트에서 가져와서 반환하고,
        # 해당 원소를 삭제한 리스트를 업데이트 한다.


# 함수명: impl_pop
# 파라미터 : index (리스트의 특정 인덱스 값을 인자로 받음), input_list(처리할 리스트)
    # 1) 입력: input_list = [1, 2, 3, 5, 6, 9]
    # 2) 출력: print(impl_pop()), print(input_list)
        # ==> 9, [1, 2, 3, 5, 6]
        # 출력: print(impl_pop(3), print(input_list)
        # ==> 5, [1, 2, 3, 6]
    # 3) 리스트의 인덱스 값이 넘는 값이 들어오면 "-1"을 출력


##############################################
user_list = input("각 수를 쉼표로 구분하시오.\ninput_list = ")
user_list = user_list.split(",")
index = input("몇번째인덱스불러오는가?(인덱스 지정하지 않으려면 x입력): ")
# input_list = [list int(user_list[u]) for u in user_list]

input_list = []
for i in user_list:
    input_list.append(int(i))

length = len(input_list)
# print(type())  # 튜플임

##############################################

def impl_pop(*args):

    if(index == ""):
        print(f"{input_list[-1]}", end="")
        input_list.remove(input_list[-1])
        print(f", {input_list}")
        # return input_list, index

    elif int(index) < length:
        # input_list.remove(input_list[args: int *args])
        print(f"{input_list[int(index)]}", end="")
        input_list.remove(input_list[int(index)])
        print(f", {input_list}")
        # return input_list

    else:
        print("-1")


print(impl_pop())
# ####################################################################################
# def impl_pop():
#
#     ##############################################
#     user_list = input("각 수를 쉼표로 구분하시오.\ninput_list = ")
#     user_list = user_list.split(",")
#     index = input("몇번째인덱스불러오는가?(인덱스 지정하지 않으려면 x입력): ")
#     # input_list = [list int(user_list[u]) for u in user_list]
#
#     input_list = []
#     for i in user_list:
#         input_list.append(int(i))
#
#     length= len(input_list)
#     # print(type(args)) #튜플임
#     ##############################################
#
#     if (length> int(index)):
#         # input_list.remove(input_list[args: int *args])
#         input_list.remove(input_list[int(index)])
#         print(f"{input_list[int(index)]},{input_list}")
#         return input_list
#     elif(index == 'x'):
#         input_list.remove(input_list[len(input_list)-1])
#         print(f"!{input_list[len(input_list)-1]}, {input_list}")
#         return input_list
#     else:
#         print("-1")

#######################################################################
#
# def impl_pop(index, input_list):
#     if (index in len(input_list)):
#         print(f"{input_list[index]}")
#         input_list.remove(index)
#         return input_list
#     elif (index == None):
#         print(f"{input_list[len(input_list)-1]}")
#         input_list.remove(input_list[len(input_list)-1])
#         return input_list
#     else:
#         print("-1")

