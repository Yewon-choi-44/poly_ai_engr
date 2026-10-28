class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2*self.w + 2*self.h
    def area_tmp(self):
        print("inh-->inh: 다중 상속/ 상속-> 상속")
        return self.w * self.h
    
class Square:
    def __init__(self, w):
        self.w = w
    def area(self):
        return self.w ** 2
    def perimeter(self):
        return 4 * self.w

class SquareInh(Rect):
    def __init__(self, w):
        super().__init__(w, w)
    def area_tmp(self):
        print("inh: 상속")
        return self.w * self.w

class Cube(SquareInh):
    def surface_area(self):
        surf_area = super(SquareInh, self).area_tmp()
        return surf_area * 6

    def volumn(self):
        vol = super().area_tmp() # SquareInh

if __name__ == '__main__':  
    rect = Rect(2,4)
    print(rect.area(), rect.perimeter())
    
    square = Square(4)
    print(square.area(), square.perimeter())

    squareInh = SquareInh(rect)
    print(squareInh.area_tmp())

    cube = Cube(squareInh)
    print(cube.surface_area(), cube.volumn())