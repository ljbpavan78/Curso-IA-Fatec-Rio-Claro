'''Peça um número e exiba a mensagem "O número é positivo." apenas se ele for
maior que zero'''
numero = float(input("Digite um número: "))
if numero > 0:
    print(f"O número {numero} é positivo")
elif numero == 0:
    print(f"O número {numero} é nulo")
else:
    print(f"O número {numero} é negativo")