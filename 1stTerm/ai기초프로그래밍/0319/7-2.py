#리스트 크기 입력
#각 원소 입력
#특정값 입력
#순차검색
num=[];
cnt=1;
while(True):
    l = int(input("리스트 크기 입력: "));
    print(f"{l}개의 정수를 입력하시오.");
    for i in range(l):
        a=int(input(""))
        num.append(a);
        
    search = int(input("찾을 값을 입력하세요: "))
    for i in range(l):
        if search == num[i]:
            print(f"{search}를 찾았습니다. 인덱스는 {num.index(search)}");
        elif cnt==l:
            print("찾을 수 없습니다.");
        else: 
            cnt+=1;
            
  # done= input("그만하시겠습니까?[y/n]: ")
   #if done == "y":
       # print("ㅃㅇ");
       # break;
   # else: 
       # print("ㄱㄱ");
        #continue;
