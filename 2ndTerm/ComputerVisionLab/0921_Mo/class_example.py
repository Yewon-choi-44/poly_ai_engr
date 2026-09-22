class FourCalc:
    def setData(self, first, second):
        self.first = first
        self.second = second
    # 생성자 (객체 생성 시 수행되는 메서드)

    def __init__(self, first=1, second=1):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

calc_0 = FourCalc(3,4)
calc_1 = FourCalc(1,2)
print(calc_0.add())
print(calc_0.sub())
print(calc_0.mul())

class MoreCalc(FourCalc): #상속
    def __init__(self, first=1, second=1, third=2):
        # self.first = first
        # self.second = second
        super().__init__(first, second)
        self.third = third

        def pow(self):
            return self.first ** self.second
        
        def add(self):
            return super().add() ** self.third
        
        def div(self):
            if self.second==0:
                return 0
            else:
                return super().div() 


# MoreCalc 클래스로부터 객체 생성, 메서드 호출 등 해보기
# mul 메서드 재정의         
