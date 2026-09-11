'''Peça o salário e o tempo de empresa (em anos) de um funcionário. Usando ifs aninhados, 
exiba "Elegível a reajuste." apenas se o salário for menor que R$2000 e o tempo de empresa
for maior ou igual a 5 anos.'''
salario = float(input("Digite o salário do funcionário: R$ "))
tempo_empresa = int(input("Digite o tempo de empresa do funcionário (em anos): "))

if salario < 2000:
    if tempo_empresa >= 5:
        print("Elegível a reajuste.")
    else:
        print("Não elegível a reajuste.")
else:
    print("Não elegível a reajuste.")
