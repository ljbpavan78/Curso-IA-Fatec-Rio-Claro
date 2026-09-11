'''Peça um número inteiro e exiba "É múltiplo de 5." apenas se ele for divisível
por 5.'''
numero = int(input("Digite um número inteiro: "))
if numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 5.")