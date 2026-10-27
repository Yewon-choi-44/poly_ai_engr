'''#인덱스

fruits = ('사과', '포도', '수박', '참외', '배','자두','복숭아','바나나');
print(fruits);
print(type(fruits));

print("="*30);

print()
print(fruits[3]);
print(fruits[len(fruits)-1]);
print(fruits.index('포도'))
print(fruits.index('바나나'))

print("="*30);



#튜플

names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민','김연아')
inputData = input("검색하려는 이름을 입력하세요.: ");
print("이름: ", inputData, ', 인덱스: ', names.index(inputData));

print("="*30);

name = ('박찬호', '이승엽', '박세리', '박지성', '이순철','선동열','손흥민','김연아')
inputData = input("검색하려는 이름을 입력하세요: ")
found=False

print("="*30);



#15페이지 빠진 부분

for index, item in enumerate(name):
    if item==inputData:
        found=True
        break;
if found == True:
    print(f"{inputData}은(는) 목록에 있으며, 인덱스는 {index}입니다.")
else:
    print("찾고자 하는 이름이 없습니다.")
    
print("="*30);
    
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue','Indigo', 'Purple')
print('Green' in colors);
print('Green' not in colors);

print("="*30);

colors=('Red', 'Orange', 'Yellow', 'Green', 'Blue','Indigo', 'Purple')
print(colors)
print('colors의 자료형: ', type(colors))

cs = sorted(colors)
print(cs)
print('cs의 자료형:', type(cs));


print("="*30);
'''



#딕셔너리 (★오늘의 하이라이트라 하심)

ages = {'박찬호': 48, "박지성": 40, "박세리": 50, "이승엽":43}
print(ages)
print(type(ages))
ages['박지성']


print("="*30);


dicContainer = {'이름': "홍길동", "나이": 25, "주소": "서대문구 연희로", "취미":['축구','수영','조깅'], "몸무게": 85.3}
print(dicContainer['취미'])
print(dicContainer['나이'])

dicContainer['나이']=30
print(dicContainer['나이'])

dicContainer['혈액형'] = "O"
print(dicContainer);

del dicContainer['혈액형']
print(dicContainer);

print(len(dicContainer))



print("="*30);


#★★★★★ keys() values() ★★★★★★

print(dicContainer.keys())
for key in dicContainer.keys():
    print(key, '\t:', dicContainer[key]);

print("="*30);

for i in dicContainer.keys():
    print(i, '\t:', dicContainer[i]);