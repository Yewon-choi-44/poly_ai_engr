score = [];
fail = 0;

for i in range(6):
    print(f"{i+1}",end="");
    s = int(input("번째 성적을 입력하세요: "));
    print("-"*4);
    score.append(s);
    if s<40:
        fail+=1;
        
avg = sum(score)/6;

print(f"\n40미만의 과목 수: {fail}");
print(f"평균 점수:{avg}");

if avg<60 or fail>0:
    print("불합격");
else:
    print("합격");
    

#############################################################

scores = [];

for i in range(6):
    print(i+1, '번째의 성적을 입력하세요',end='');
    scores.append(int(input()));
    
total = 0
undersubject = 0;

for score in scores:
    if score <= 40:
        undersubject+=1;
    total +=score
print("40점 미만의 과목 수: ", undersubject);
average =total/len(scores)
print(f"평균점수: {average:.2f}")