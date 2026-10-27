#while문을 사용해 1~100까지 3의 배수 합 출력

sum_ = 0;
cnt = 0;

while cnt<100:
    cnt+=1;
    
    if cnt % 3 == 0:
        sum_+=cnt;
        print(f"지금까지의 합은: {sum_}");
            
    elif cnt == 100:
        break;

print(f"최종합은: {sum_}");


