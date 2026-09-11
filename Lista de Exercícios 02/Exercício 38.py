'''Peça um número de 1 a 12 representando o mês e exiba a estação do ano 
correspondente (verão, outono, inverno ou primavera), usando elif.'''
mes = int(input("Digite o mês do ano, conforme exemplo (1 = Janeiro, 2= Fevereiro) "))
if mes == 12 or mes == 1 or mes == 2:
    print("Verão")
elif mes == 3 or mes == 4 or mes == 5:
    print("Outono")
elif mes == 6 or mes == 7 or mes == 8:
    print("Inverno")
elif mes == 9 or mes == 10 or mes == 11:
    print("Primavera")
else:
    print("Mês inválido! Digite um número de 1 a 12.")