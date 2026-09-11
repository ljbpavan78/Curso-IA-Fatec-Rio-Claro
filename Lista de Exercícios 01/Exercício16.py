"""Peça ao usuário o nome, o salário atual (número decimal) e o percentual de
aumento (número decimal, ex.: 10 para 10%). Calcule o novo salário após o aumento
e exibe uma frase completa com o nome da pessoa e o valor final."""
nome = input("Digite o nome da pessoa: ")
salarioatual = float(input("Digite o salário atual (ex.: 2500.00): "))
percentualaumento = float(input("Digite o percentual de aumento (ex.: 10 para 10%): "))
novosalario = salarioatual + (salarioatual * percentualaumento / 100)
print("O novo salário de " + nome + " é R$ " + str(novosalario))