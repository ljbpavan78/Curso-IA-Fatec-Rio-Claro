'''Peça o saldo de uma conta bancária e exiba "Atenção: saldo negativo." apenas se
o saldo for menor que zero.'''
saldo = float(input("Digite o saldo da conta bancária: "))
if saldo < 0:
    print("Atenção: saldo negativo.")