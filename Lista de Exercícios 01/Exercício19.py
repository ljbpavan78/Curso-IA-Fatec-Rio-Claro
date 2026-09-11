"""Peça ao usuário a quantidade de horas trabalhadas no mês e o valor que ele
recebe por hora. Calcule o salário bruto (horas x valor da hora) e exiba o resultado
formatado em uma frase."""
horastrabalhadas = float(input("Quantas horas você trabalhou no mês? ex.: 160: "))
valorrecebidoporhora = float(input("Quanto você recebe por hora? ex.: 25.50: "))
salariobruto = horastrabalhadas * valorrecebidoporhora
print("O seu salário bruto é R$ " + str(salariobruto))