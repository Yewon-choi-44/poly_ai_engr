score = open(r'C:/Users/AI-00/Downloads/text.txt','r')
#lines = score.readlines()
#print("lines:", lines)
#for i in lines:
#    print("i",i, end="")
line = score.readline()
    
while line != "":    
    print("\nline:", line)
    line = score.readline()


