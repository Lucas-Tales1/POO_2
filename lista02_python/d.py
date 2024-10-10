import math

print("Digite a base e a altura do retângulo")
base = int(input())
altura = int(input())
area = base*altura
perimetro = 2*base + 2*altura
diagonal = math.sqrt(base*base + altura*altura)
print(f"Área = {area:.2f} - Perímetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}")