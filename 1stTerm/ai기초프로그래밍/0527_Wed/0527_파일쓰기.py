num_list = ['11','22','33']
outfile = open('numbers.txt','w')
outfile.writelines(num_list)
outfile.close()
print('numbers.txt 파일이 생성되었음')