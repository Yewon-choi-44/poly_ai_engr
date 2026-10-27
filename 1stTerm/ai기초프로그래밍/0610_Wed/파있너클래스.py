class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
name = input("당신의 이름은 무엇입니까?")
age = int(input("당신의 나이는 몇 살입니까?"))
st = Student(name, age)

print(f"당신의 이름은 {st.name}이고" , end=' ')
print(f"나이는 {st.age}세이군요.")