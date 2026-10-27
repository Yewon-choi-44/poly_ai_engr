class Rectangle:
    def __init__(self, width, height):
        self.width = width #생성자, 초기화 메서드
        self.height = height
        
    def area(self):
        return self.width*self.height
        #print("rec1의 면적은 {}입니다.".format(self.width*self.height))  

    
r1 = Rectangle(5, 3)
rec1 = r1.area()
print("rec1의 면적은 {rec1}입니다.")