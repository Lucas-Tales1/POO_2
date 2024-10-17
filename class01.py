class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calcArea(self):
        return self.b * self.h / 2

x = Triangulo()
x.b = 5
x.h = 8
print(x.b,x.h)
y = Triangulo()
y.b = 10
y.h = 20
print(y.b,y.h)
z = y
z.b = 15
z.h = 30
print(y.b,y.h)
print(x.calcArea()) #Triangulo.calcArea(X)
print(y.calcArea())

