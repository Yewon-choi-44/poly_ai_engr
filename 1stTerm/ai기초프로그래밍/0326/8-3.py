#name_ = {"철수", "영희"}
#user_Num={""}
#print("1. 연락처 추가 \n2. 연락처 조회 \n3. 종료");
#select = int(input("메뉴를 선택하세요: "));

# 딕셔너리 추가해서 입력받은 자료를 저장할 공간 만들기.
# 인덱스로 
print("1. 연락처 추가 \n2. 연락처 조회 \n3. 종료");
select = int(input("메뉴를 선택하세요: "));
usernum={};
userindex={}; 
num = {"철수":"010-1111-1111", "영희":"010-2222-2222","민수":"010-3333-3333", "지혜":"010-4444-4444"};

while(True):

   # name = {"철수": 1 , "영희":2 , "민수":3 , "지혜":4 };
   # user_Num = {1:"010-1111-1111", 2:"010-2222-2222", 3:"010-3333-3333" , 4:"010-4444-4444"};
   
  
    #얘가 초기화가 되면 안된다고 그럼 어디다 둬야 하나?

   #user_Num을 하나 더 만들어서 입력받는 거 넣으라는 거였잖냐 맞는거맞나 아 너무 멍청애
   # ^^ 위에 거 아니고 이름/전번 두 개 딕셔너리로 나눠서 인ㄱ덱스로 찾느게 맞는 것 같아 ㅁ 언니말이이거였다고 ㅇ나ㅣ라ㅣㅇㄴ라지ㅏㄷ
   # keys() value()를...
   #print(f"{usernum}"); 
   
   if select == 1:
        
        
        name = input("이름을 입력하세요: ");
        #usernum[name] = input("전화번호를 입력하세요: ");
        phone = input("전화번호를 입력하세요: ");
        
        #userindex[phone]
      #  userindex[phone] = name
        #serindex[usernum[name]] = len(userindex)+1;
        
        #name[name_] = len(name)+1;
        #user_Num[Input_Num] = len(user_Num)+1;
        
        print(f"입력정보확인: {usernum[name]}");
        print(f"{name}의 연락처가 저장되었습니다.");
        break;
             
   elif select == 2:
       user=input("조회할 이름을 입력하세요: \n");
       print(user, " 의 전화본호: ",{usernum[user]});
       #Phn_Num[name] = Input_Num
       # print(f"{name['name_']}의 전화번호: \n{user_Num['name_.values(name_)']}");
       break;
        
   elif select == 3:
        print("프로그램을 종료합니다.");
        break;
            
   else: 
        print("올바른 번호를 입력하세요.")
        continue;
    
    


