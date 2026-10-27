i=0;
#ps=input("관리자 암호를 입력하세요: ");
 
while i < 5 :
    ps=input("관리자 암호를 입력하세요: ");
    
    if i == 4: 
        print("로그인 실패 횟수 초과");
        break;
    if ps == 'hanbitac':
            print("로그인 됐습니다.");
            break;
            
    elif ps != "hanbitac":
            i+=1;
            print("암호를 다시 확인하세요.\n");
            
'''
pw = "hanbitac";
cnt = 1;

while True:
    if cnt > 6 :
        print("로그인 실패 횟수 초과");
        break;
        
    inputPw = input("관리자 암호를 입력하세요.");
    
    if inputPw != pw:
        print("암호를 다시 확인하세요! \n");
        cnt+=1;
    elif inputPw == pw:
        print("로그인 됐습니다.");
        break;
       
    
'''    
    
    
    
'''   
adminPw = "hanbitac";
count=1;
    
while True:
        if count > 6:
            print("로그인 실패! 횟수 초과!");
            break;
            
        inputPw = input('관리자 암호를 입력하세요.');
        
        if inputPw != adminPw:
            print("암호를 다시 확인하세요!");
            count +=1;
        elif inputPw == adminPw:
            print("로그인 됐습니다.");
            break;
    '''