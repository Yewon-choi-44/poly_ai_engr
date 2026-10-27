infile = open(r"C:\Users\AI-00\Downloads\text2.txt",'r', encoding='utf-8')

line_cnt = 0
word_cnt = 0
char_cnt =0

line = infile.readline()

while line != "":
    line_cnt += 1
    words =line.strip().split()
    word_cnt += len(words)
    char_cnt += len(line.strip())
    
    line = infile.readline()
    
infile.close()

print(f"라인 수: {line_cnt}")
print(f"단어 수: {word_cnt}")
print(f"문자 수: {char_cnt}")