import math
class circulo:
    def __init__(self):
        self.raio = 0
    def calc_area(self):
        math.pi * (self.raio * self.raio)
    def calc_circunferencia(self):
        2 * math.pi * self.raio

x = circulo()
x.raio = float(input("Digite o valor do raio: "))
print(f"Área: {x.calc_area()}")
