#infile = open(r"C:\Users\AI-00\Downloads\` 이름 최예원.txt", 'r')
'''lines = infile.read()
infile.close()
print(lines)
line_list = lines.split()
print(line_list)
'''

#infile=open(r"C:\Users\AI-00\Downloads\111111111111111.txt","r")
'''
text = infile.read(10)
while text != "":
    print(len(text))
    text=infile.read(10)
print(len(text))
infile.close()
'''

infile = open(r"C:\Users\AI-00\Downloads\111111111111111.txt","r")
line = infile.readline()
while line != ""win08130
:
    print(line)
    line = infile.readline()
infile.close()