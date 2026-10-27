import pandas as pd
usernum = {}
userindex = {}
num = {"철수":"010-1111-1111", "영희":"010-2222-2222","민수":"010-3333-3333", "지혜":"010-4444-4444"}

while(True):

    print("1. 연락처 추가 \n2. 연락처 조회 \n3. 종료")
    select = int(input("메뉴를 선택하세요: "))

    if select == 1:
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")

        usernum[name] = phone   # ⭐ 이거 추가!!

        print(f"입력정보확인: {usernum[name]}")
        print(f"{name}의 연락처가 저장되었습니다.")

    elif select == 2:
        user = input("조회할 이름을 입력하세요: ")

        if user in usernum:
            print(user, "의 전화번호:", usernum[user])
        else:
            print("해당 이름이 없습니다.")

    elif select == 3:
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력하세요.")