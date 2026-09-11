'''Peça ao usuário um número e exiba o resultado da expressão que utiliza not
para verificar se o número não está entre 10 e 20'''
numero = float(input("Digite um número: "))
resultado = not (numero >= 10 and numero <= 20)
print("O número NÃO está entre 10 e 20? ", resultado)