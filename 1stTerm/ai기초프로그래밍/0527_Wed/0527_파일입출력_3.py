textKor = open(r'C:/Users/AI-00/Downloads/text2.txt','r')
line = textKor.readline()

cnt = 0

while line != "":
    print(line, end="")
    line = textKor.readline()
    cnt += 1