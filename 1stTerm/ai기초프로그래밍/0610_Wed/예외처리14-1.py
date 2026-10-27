# 사용자로부터 회원 정보를 입력받아 회원 등록 프로그램을 작성하시오.
# 단, 나이 입력 시 발생할 수 있는 오류를 예외처리 하도록 한다. 

# [구현 조건]
# 1) 사용자로부터 이름과 나이를 입력받는다.
# 2) 이름에 exit를 입력하면 더 이상 입력을 종료한다.
# 3) 나이는 정수로만 입력 가능하며, 숫자가 아닌 값을 입력하면
#     "나이는 숫자만 입력해야 합니다"를 출력한 뒤, 해당 이름은 등록 실패로 기록합니다.
# 4) 정상 입력된 회원 정보는 (이름, 나이) 형식으로 저장합니다.
# 5) 입력 종료 후 전체 등록 된 회원 목록을 출력합니다.
#     - 나이 입력에 실패한 경우 "등록 실패"로 표시합니다.


###############################################################################
# while문 사용. 저 안에서 입력 받고 if문으로 판단.
# 여러 명 입력 받아야 하므로 리스트? 딕셔너리?로? 저장

Hwe = {}

while(True):
    HweName = input("이름을 입력하세요 (종료: exit): ")
    
    if HweName == "exit":
        break
    

    
    try:
        HweAge = int(input("나이를 입력하세요: "))
        Hwe[HweName] = HweAge
        print()
        
    except AttributeError:
        print("나이는 숫자만 입력해야 합니다.")
        Hwe[HweName] = "등록 실패"
        print()
        continue    
        # print(f"{HweName} - 등록 실패 \n")
    except ValueError:
        print("나이는 숫자만 입력해야 합니다.")
        Hwe[HweName] = "등록 실패"
        print()
        continue    
        

    


print("\n\n")
print("======= 회원 등록 시스템 ======")
HweListKey = list(Hwe.keys())
HweListVal = list(Hwe.values())



#####################################

# # 오류 1 

# ======= 회원 등록 시스템 ======
# 홍길동 - 이순신
# 35 - 등록 실패

# 수정: for i,j in HweListKey, HweListVal 에서
        # for i in range(len(HweListKey)) 로 변경
        
#####################################

# 오류 2

# ======= 회원 등록 시스템 ======
# 홍길동 - HweListVal0
# 이순신 - HweListVal1

# 수정:  print(f"{HweListKey[i]} - HweListVal{i}") 에서
         # print(f"{HweListKey[i]} - {HweListVal[i]}") 로 수정 

#####################################


for i in range(len(HweListKey)):
    # print(f"{Hwe.keys()} - {i.values()}")
    print(f"{HweListKey[i]} - {HweListVal[i]}")
    

outfile = open('members.txt','w')

# for i in range(len(HweListKey)):
#     # outfile.write(HweListKey[i] + " - " + HweListVal[i])
    
for i in HweListKey:
    outfile.writelines(i + " - ")

for i in HweListVal:
    outfile.writelines(i)

    
    
outfile.close()



# exit()



































# ################################################################################
# # 젬코드

# print("=== 회원 등록 시스템 ===")
# members = []  # 회원 정보를 저장할 빈 리스트(목록)를 만듭니다.

# while True:
#     name = input("이름을 입력하세요 (종료: exit): ")
    
#     # 'exit'이 입력되면 무한 반복을 멈춥니다.
#     if name == 'exit':
#         break

#     age_input = input("나이를 입력하세요: ")

#     try:
#         # 입력받은 글자를 정수(숫자)로 변환을 시도합니다.
#         age = int(age_input)
#         # 성공하면 (이름, 나이) 형태로 목록에 추가합니다.
#         members.append((name, age))
#         print("등록 완료!\n")
        
#     except ValueError:
#         # 숫자로 바꿀 수 없는 값(예: '스무살')이 들어오면 에러가 나면서 이곳이 실행됩니다.
#         print("나이는 숫자만 입력해야 합니다.\n")
#         # 에러가 났으므로 나이 대신 "등록 실패"라는 글자를 저장합니다.
#         members.append((name, "등록 실패"))

# # 프로그램 종료 후 전체 목록 출력
# print("\n[등록된 회원 목록]")
# for name, age_info in members:
#     if age_info == "등록 실패":
#         print(f"{name} - {age_info}")
#     else:
#         print(f"{name} - {age_info}세")