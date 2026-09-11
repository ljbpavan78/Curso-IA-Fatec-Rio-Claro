'''Peça ao usuário um número e exiba se ele está fora do intervalo de 10 a 20
(menor que 10 ou maior que 20), utilizando o operador or.'''
numero = float(input("Digite um número: "))
resultado = numero < 10 or numero > 20
print("O número está fora do intervalo entre 10 e 20? ", resultado)