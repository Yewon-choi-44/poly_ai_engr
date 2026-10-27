'''
fruit = ['사과','포도','수박','참외','배','자두','복숭아','바나나'];
print(fruit);

print("="*30);

print(fruit[0]);
print(fruit[1]);
print(fruit[2]);

print("="*30);

for i in range(1,len(fruit),2):
    print(f"fruit{[i]}: {fruit[i]}");
    
print("="*30);
    
message = input('메시지를 입력하세요. ');
print(len(message))

print("="*30);

balls = ['야구공', '축구공', '탁구공', '골프공', '농구공'];

for item in balls:
    print('item: ', item);
    
    
print("="*30);

for index, item in enumerate(balls):
    print('index: ', index, ' item: ', item);
    
print("="*30);


while i < len(balls):
    print(balls[i]);
    i+=1;
    
print("="*30);

hobby = ['독서', '등산', '요리'];
print("홍길동 학생의 취미: ", hobby);

hobby.append('배구');
print('홍길동 학생의 취미:', hobby);

print("="*30);

countries = ['korea', 'china', 'japan'];
print(countries);
countries.insert(1,'usa');
print(countries);

print("="*30);
'''
languages = ['C/C++', 'C#', 'java','python'];
print(languages);
languages.remove('java');
print(languages);

print("="*30);



for str in languages:
    if str == 'java':
        languages.remove('java');
print(languages);

print("="*30);

while ('java' in languages):
    languages.remove('java');
print(languages);

print("="*30);

animals = ['호랑이', '사자', '곰', '여우', '늑대'];
print(animals);
print(animals[:3]);
print(animals[3:]);
print(animals[len(animals)-2:]);



