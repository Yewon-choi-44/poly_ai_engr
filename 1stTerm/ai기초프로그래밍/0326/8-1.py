menu = ('김밥', '라면', '돈까스', '떡뽁이');
MyPick = input("주문할 메뉴를 입력하세요: ");

if MyPick == "김밥":
    print(f"{MyPick}의 가격은 3000원입니다.");
elif MyPick =="라면":
    print(f"{MyPick}가격은 4000원입니다.");
elif MyPick == "돈까스":
    print(f"{MyPick}의 가격은 7000원입니다.");
elif MyPick == "떡뽁이":
    print(f"{MyPick}의 가격은 5000원입니다.");
else:
    print("그딴 메뉴는 없습니다. 메뉴판을 똑바로 보시오.");
    
    
#딕셔너리로 바꾸자. 
#그냥 두자.

#menu = ('김밥')