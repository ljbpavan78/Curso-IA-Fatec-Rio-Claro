''' Peça ao usuário um número inteiro e exiba o resultado da expressão que
verifica se ele é par e maior que 10 ao mesmo tempo (combine % com and)'''
numero = int(input("Digite um número inteiro: "))
resultado = numero % 2 == 0 and numero > 10
print(f"O número {numero} é par e maior que 10? {resultado} ")