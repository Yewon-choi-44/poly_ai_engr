"""
다형성
-오버라이딩 (고객 등급별 계산이 상이함)
-silver, gold

def calculate_grade(custom_grade):
    if custom_grade == 'silver':
        discount = 0
        bonus = 0.05
    elif custom_grade == 'gold':
        discount = 0.1 
        bonus = 0.3
==> 추가적인 등급 발생 시 메서드를 변경해야 함.
--> 기본 customer class 상속 받아서 
    계산하는 메서드만 수정해서 사용
"""

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.bonus_points = 0
        self.grade = 'SILVER'
        self.bonus_ratio = 0.05
    
    def calc_price(self, price):
        self.bonus_points += (price * self.bonus_ratio)
        return self.bonus_points

class GoldCustomer(Customer):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.grade = "GOLD"
        self.bonus_ratio - 0.1
        self.discount_ratio = 0.05

    def calc_price(self, price):
        self.bonus_points += (price * self.bonus_ratio)
        price = price - price * self.discount_ratio
        return self.bonus_points

## class --> vip, agent-Id
## main문 작성해서 확인해볼 것

if __name__ == '__main__':
    customer_silver = Customer(100, 'kim')
    customer_gold = GoldCustomer(200,'lee')
    customer_silver.calc_price(100)