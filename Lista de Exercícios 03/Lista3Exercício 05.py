'''Peça ao usuário 5 números, um de cada vez, e calcule a soma total deles usando while.'''
soma = 0
i = 0
while i < 5:
    numero = float(input("Digite um número: "))
    soma += numero
    i += 1
print(f"A soma total dos números é: {soma}")