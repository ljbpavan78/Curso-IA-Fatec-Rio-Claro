"""Peça dois números ao usuário e exiba, em print() separados, o resultado
da soma, subtração, multiplicação e divisão entre eles."""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print("A soma dos dois números é: " + str(soma))
print("A subtração dos dois números é: " + str(subtracao))
print("A multiplicação dos dois números é: " + str(multiplicacao))
print("A divisão dos dois números é: " + str(divisao))