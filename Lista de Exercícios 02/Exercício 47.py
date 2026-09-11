'''Peça três números diferentes e, utilizando ifs aninhados (sem usar a função
max()), determine e exiba qual dos três é o maior.'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2:
	if numero1 > numero3:
		maior = numero1
	else:
		maior = numero3
else:
	if numero2 > numero3:
		maior = numero2
	else:
		maior = numero3

print(f"O maior número é {maior}.")