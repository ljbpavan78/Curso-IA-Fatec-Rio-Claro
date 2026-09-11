"""Peça dois números inteiros ao usuário (um de cada vez, com input()), 
converta ambos para int() e exiba a soma dos dois, concatenando o resultado 
em uma frase."""
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma = num1 + num2
print("A soma dos dois números é: " + str(soma))