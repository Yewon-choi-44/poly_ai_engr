class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_details(self):
        print('이름: ', self.name, '나이:' , self.age)
        
class Student(Person):
    def __init__(self, name, age, department):
        Person.__init__(self, name, age)
        self.department = department
        
    def print_details(self):
        print('이름: ', self.name, '나이: ', self.age, '학과: ', self.department)

class Professor(Person):
    def __init__(self, name, age, major):
        Person.__init__(self, name, age)
        self.major = major
    def print_details(self):
        print('이름: ', self.name, '나이: ', self.age, '전공: ', self.major)
        

#메인 프로그램 

Pname = input("일반인의 이름을 입력하시오: ")
Page = int(input("일반인의 나이를 입력하시오: "))
person1 = Person(Pname, Page)
person1.print_details()
print()

Sname = input("학생의 이름을 입력하시오: ")
Sage = int(input("학생의 나이를 입력하시오: "))
Sdep = input("학생의 학과를 입력하시오: ")
student1 = Student(Sname, Sage, Sdep)
student1.print_details()
print()


Proname = input("교수의 이름을 입력하시오: ")
Proage = int(input("교수의 나이를 입력하시오: "))
Prodep = input("교수의 전공을 입력하시오: ")
professor1 = Professor(Proname, Proage, Prodep)
professor1.print_details()
print()
# person1.print_details()
# student1.print_details()
#professor1.print_details()