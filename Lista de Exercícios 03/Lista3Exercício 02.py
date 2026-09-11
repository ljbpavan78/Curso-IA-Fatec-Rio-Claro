'''Peça ao usuário um número N e, usando while, conte de N até 1 
(ordem decrescente), imprimindo cada número.'''
numero = int(input("Digite um número: "))
contador = numero
while contador >0:
    print(contador)
    contador -=1