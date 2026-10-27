#2. 앞의 Rectangle 클래스에 사각형 둘레 계산, 
#사각형의 정보(가로, 세로, 면적, 둘레)를 출력하는 메소드를 추가하여 구현하시오.

#가로 5, 높이 3인 사각형의 정보 메소드 출력 예
#사각형의 가로: 5
#사각형의 높이: 3
#사각형의 면적: 15
#사각형의 둘레: 16


class Rectangle:
    def __init__(self, width, height):
        self.width = width #생성자, 초기화 메서드
        self.height = height
        
        
    def area(self):
        print(f"사각형의 면적: {self.width*self.height}")  
        return self.width*self.height

    def surface(self):
        print(f"사각형의 둘레: {2*self.width + self.height}")
        return (2*self.width + self.height)
        
    def info(self):
        print(f"사각형의 가로: {self.width}")
        print(f"사각형의 세로: {self.height}")
        
    
r1 = Rectangle(5, 3)


recInfo = r1.info()
rec1 = r1.area()
sur1 = r1.surface()



#print(f"사각형의 가로: {r1}")
#print(f"사각형의 세로: {}")
#print(f"사각형의 면적: {rec1}")
#print(f"사각형의 둘레: {sur1}")