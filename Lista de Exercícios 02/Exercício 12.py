'''Peça ao usuário um número e exiba se ele está entre 10 e 20 (maior que 10
e menor que 20) utilizando o operador and'''
numero = float(input("Digite um número maior que 10 e menor que 20: "))
resultado = numero > 10 and numero < 20
print("O número está entre 10 e 20? ", resultado)