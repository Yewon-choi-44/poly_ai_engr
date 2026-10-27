import pandas as pd

print("1. 연락처 추가 \n2. 연락처 조회 \n3. 종료");
select = int(input("메뉴를 선택하세요: "));
usernum={};
num = {"철수":"010-1111-1111", "영희":"010-2222-2222","민수":"010-3333-3333", "지혜":"010-4444-4444"};
num_data = pd.DataFrame(num,columns=num.keys())

#print(num_data)

while(True):
    if select == 1:
         name = input("이름을 입력하세요: ");
         phone = input("전화번호를 입력하세요: ");
         num[name] = phone
         #num_data = pd.DataFrame(num)
         print(f"입력정보확인: {usernum[name]}");
         print(f"{name}의 연락처가 저장되었습니다.");
         break;
              
    elif select == 2:
        user=input("조회할 이름을 입력하세요: \n");
        print(f"{num_data[user]}");
        break;
         
    elif select == 3:
         print("프로그램을 종료합니다.");
         break;
             
    else: 
         print("올바른 번호를 입력하세요.")
         continue;
     