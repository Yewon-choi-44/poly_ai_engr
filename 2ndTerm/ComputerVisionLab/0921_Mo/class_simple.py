# 객체 지향 언어 이해. 자바랑 비교 등
# 객체 지향: 객체를 정의하는 것부터 시작...
# 아침에 일어나서 학교를 가는 과정
# 절차 지향
# 일어난다(wakeup) -> 씻는다(wash) -> 밥는다(eat) -> 벗스탄다(takebus) -> 요금지불(tag) -> 학교당

# 객체 지향은 기본적으로
    # 1) 학생 클래스, 버스/지하철/택시 클래스 있어야 함. 학교/집 클래스 있어야 함.
    # 2) 각 객체가 제공하는(수행하는) 기능을 구현(메서드)
    # 3) 각 객체가 제공하는 기능들 간의 소통(메시지 전달) 객체 간 협력 구현 가능
    # std 객체에서 bus 객체의 메서드를 호출...


"""
java, class name=file name
Student.java
public class Student {
    //member 변수 정의
    public String stdName;
    public int grade;
    public static String stdSchoolName;

    // 생성자
    public Student(String StdName, int grade) {
        this.stdName = stdName; 
        this.grade = grade;
    }

    // Method 
    public String showInfo() {
        return stdName + ...;
    }
}


Student std1 = new Student('shin', 1);

"""


### python

class Student:
    SchoolName = "polytechnics" # class 변수
    def __init__(self, name, money):
        self.name = name 
        self.grade = 1
        self.money = money


    def takeBus(self, bus):
        bus.take(1500)
        self.money = self.money - 1500

    def takeSubway(self, subway):
        subway.take(1500)
        self.money = self.money - 1500

    def showInfo(self):
         print(f"{self.name}학생이 가진 돈은 현재 {self.money}원 입니다.")
            
class Bus:
    def __init__(self, busNum):
        self.busNum = busNum
        self.numPassenger = 0
        self.money = 0

    def take(self, money):
        self.numPassenger += 1
        self.money += money

    def showInfo(self):
        print(f"{self.busNum}번 버스의 승객은 {self.numPassenger}이고, 현재 수입은 {self.money}원 입니다.")

class Subway:
    def __init__(self, lineNum):
        self.lineNum = lineNum
        self.numPassenger = 0
        self.money = 0

    def take(self, money):
        self.numPassenger += 1
        self.money += money

    def showInfo(self):
        print(f"{self.lineNum}번 버스의 승객은 {self.numPassenger}이고, 현재 수입은 {self.money}원 입니다.")




# 객체 생성
std1 = Student('이승재', 10000)
std2 = Student('홍승현', 20000)
std3 = Student('김지수', 30000)

bus420 = Bus(420)
subway1 = Subway(1)

# 메서드 호출 등 수행
std1.takeBus(bus420)
std2.takeBus(bus420)
std3.takeSubway(subway1)


std1.showInfo()
std2.showInfo()
std3.showInfo()

bus420.showInfo()
subway1.showInfo()



# 택시 클래스 하나 만들기 (생성자에서 택시 이름 등도 고민)
# 학생도 추가해보기.
# 학생, 버스, 지하철 클래스에 추가 메서드도 추가해서 확인해보기.