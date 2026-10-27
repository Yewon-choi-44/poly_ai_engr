score = open(r'C:/Users/AI-00/Downloads/score.txt','r')
lines = score.readlines()
print(lines)

sum=0
cnt=0
max=0
min=100

scoreInt=[]
for i in lines:
    print(i, end="")
    scoreInt.append(int(i))
    
for i in range(len(scoreInt)):
    sum+=int(s coreInt[i])
    cnt+=1
    
    if int(scoreInt[i]>max):
        max = int(scoreInt[i])
    
    elif int(scoreInt[i]<min):
        min = int(scoreInt[i])
        
print()
print("총점: ", sum)
print("평균: ", sum/cnt)
print("최고점: ", max)
print("최저점: ", min)