#중첩 반복문을 이용해 2~9단까지 구구단 출력
for i in range(2,10):
    print(f"{i}단");
    for j in range(1,10):
        print(f"{i} * {j} = {i*j} ");
    print("\n");
