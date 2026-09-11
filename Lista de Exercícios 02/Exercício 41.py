'''Peça um número de 1 a 7 e exiba o dia da semana correspondente (1 = Domingo, 2 = Segunda,
..., 7 = Sábado), usando elif'''
dia = int(input("Digite um número de 1 a 7 para representar o dia da semana: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Número inválido. Por favor, digite um número de 1 a 7.")