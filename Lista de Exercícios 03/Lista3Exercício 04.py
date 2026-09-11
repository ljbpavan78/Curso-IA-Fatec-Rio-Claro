'''Usando while e uma variável acumuladora, calcule e exiba a soma de todos os
números inteiros de 1 até 10.'''
contador = 1
soma = 0
while contador<=10:
    soma = soma + contador
    print(f"Contador: {contador} | Soma atual: {soma}")
    contador = contador + 1
    