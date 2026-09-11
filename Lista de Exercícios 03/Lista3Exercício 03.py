'''Peça ao usuário um número N e, usando while, conte de N até 0. No final, 
exiba a mensagem "Liberado vôo".'''
numero = int(input("Digite um número: "))
contador = numero
while contador >=0:
    print(contador)
    contador = contador - 1
print("Liberado vôo")