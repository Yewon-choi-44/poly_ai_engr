import math
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def info(self):
        print(f"현재 좌표: ({self.x}, {self.y})")
        print(f"원점 까지의 거리: {math.sqrt(self.x**2 + self.y**2)}")
        
        
dis = Point(3,4)
dis.info()