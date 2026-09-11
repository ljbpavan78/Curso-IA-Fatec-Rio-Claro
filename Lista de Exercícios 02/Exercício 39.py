'''Peça o peso e a altura de uma pessoa, calcule o IMC (peso / altura²) e classifique o resultado
usando elif: Abaixo do peso (IMC < 18.5), Peso normal (IMC < 25), Sobrepeso (IMC < 30)
e Obesidade (IMC >= 30).'''
# Solicitando o peso e a altura do usuário
peso = float(input("Digite o seu peso em kg (ex: 70.5): "))
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# Calculando o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

# Exibindo o valor do IMC formatado com duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Classificando o resultado usando elif
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")