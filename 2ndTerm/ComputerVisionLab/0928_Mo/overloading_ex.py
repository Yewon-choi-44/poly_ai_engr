from multipledispatch import dispatch



class Student:
    @dispatch()
    def __init__(self):
        self.id = 0
        self.name = ""
        self.grade = 0

    #id, name
    
    @dispatch(int, str)
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grade = 0

    #id, name, grade

    std1 = Student()
    std2 = Student(20001000, "Kim")
    std3 = Student(20001001, "Lee", 2)

    # 필요한 패키지 등 설치 및 테스트 해볼 것.
    