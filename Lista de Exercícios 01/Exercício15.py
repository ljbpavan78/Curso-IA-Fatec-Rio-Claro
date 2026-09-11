"""Peça ao usuário a base e a altura de um triângulo e calcule sua área, usando
a fórmula área = (base * altura) /2."""
base = float(input("Digite o valor da base do triângulo (ex.: 5.5): "))
altura = float(input("Digite o valor da altura do triângulo (ex.: 3.0): "))
area = (base * altura) / 2
print("A área do triângulo é: " + str(area))