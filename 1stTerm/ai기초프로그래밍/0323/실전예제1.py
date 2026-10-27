math = ("3+2", "5/2", "10-2", "10^2*2", "1-(10%4)", "2^4", "4/2");
correct = 0;
wrong = 0;
total=0;

for i in range(len(math)):
    print(f"문제 : {math[i]}");
    answer = int(input("정답을 입력하세요.: "));
    
    if int(math)==answer:
        correct+=1;
    else: 
        wrong+=1;
        
        
print("-"*30);
print(f"정답 개수: {correct}");
print(f"오답 개수: {wrong}");
print(f"Total Score: {total}");