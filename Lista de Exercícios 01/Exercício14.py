"""Peça ao usuário o valor de um lado de um quadrado e calcule a área (lado x lado)
e o perímetro (lado x 4) exibindo os dois resultados."""
lado = float(input("Digite o valor do lado do quadrado (ex.: 3.5): "))
area = lado * lado
perimetro = lado * 4
print("A área do quadrado é: " + str(area))
print("O perímetro do quadrado é: " + str(perimetro))