# a = [1,2,[3,4,['life','is']]]
# print(a[2][2][0])




lst = [1,2,3]
dst = {i : i*2 for i in lst}
print(f"dst: {dst}")
s = set(dst.values())
print(f"s: {s}")
lst[0] = 99
print(f"lst: {lst}")
dst[2] = 7
print(f"dst: {dst}")
s.add(99)
print(f"s: {s}")
print(len(s & set(dst.values())))

asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.remove('일본')
asia.update({'한국', '홍콩', '태국'})
print(asia)


a = "engineer information programming"
b = a[:3]
c = a[4:6]
d = a[29:]
e = b + c + d
print(e)