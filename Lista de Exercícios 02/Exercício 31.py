'''Peça dois números diferentes e informe qual dos dois é o maior, usando uma 
estrutura if/else.'''
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}")
elif numero1 == numero2:
    print("Os números digitados são iguais")
else:
    print(f"O número {numero2} é maior que o número {numero1}")