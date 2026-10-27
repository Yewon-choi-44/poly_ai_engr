#1.
'''class A:
    def __init__(self):
        self.func(33)
        print("클래스 A안에서 i: ", self.i)
    def func(self, i):
        self.i=2*i
        
class B:
    def __init__(self):
        super().__init__()
    def func(self,i):
        self.i=3*i
b=B()
print(B())
'''

#2. 
'''
class A_class:
    def __init__(self):
        self.v=0
        
    def f(self):
        self.v=self.v+1
        return self.v
    
x = A_class()
print(x.f()+x.f())
'''

#3.
''' 
class My_class:
    def __init__(self, value):
        self.value=value
        
x = My_class(10)
y = My_class(20)

if x==y:
    t = My_class(x.value + y.value)
else:
    t=My_class(x.value - y.value)
print(t.value)
'''

#4. 
'''
class Account:
    def __init__(self, id):
        self.id=id
        print("self.id: ", self.id)
        id = 666
        print("id: ", id)
        print("self.id: ",self.id)
        id = self.id+id
        print("self.id", self.id)
        
        print("id: ", id)
        
acc = Account(123)
print("acc.id: ", acc.id)
'''

#5
'''
class A:
    def __init__(self):
        self.i=2
        print("self.i: ", self.i)
    def m(self):
        self.i=10
        print("self.i: ", self.i)

class B(A):
    def m(self):
        print("self.i: ", self.i)
        self.i+=2
        print("self.i: ", self.i)
        return self.i
b=B()
print(b.m())
'''

#6
class Car:
    def __init__(self, color, model):
        self.color =  color
        self.model = model
        
    def update(self, color, model):
        color = color
        self.model = model
    
    def print_car(self):
        print('이 자동차는 ' + self.color + ' ' + self.model + '.')
        
car1 = Car('빨강', '페라리')
car1.update('노랑', '포르셰')
car1.print_car()