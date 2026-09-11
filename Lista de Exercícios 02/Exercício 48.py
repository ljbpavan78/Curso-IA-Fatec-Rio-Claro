'''Peça um ano e verifique se ele é bissexto utilizando estruturas de if aninhadas
(sem usar and/or diretamente na mesma linha), seguindo a lógica: um ano é bissexto
se for divisível por 4; entre os divisíveis por 4, os divisíveis por 100 só são 
bissextos se também forem divisíveis por 400.'''
ano = int(input("Digite um ano: "))

# 1. Primeira camada: É divisível por 4?
if ano % 4 == 0:
    # 2. Segunda camada: É divisível por 100?
    if ano % 100 == 0:
        # 3. Terceira camada: É divisível por 400?
        if ano % 400 == 0:
            print("É bissexto.")
        else:
            print("Não é bissexto.")
    else:
        # Se for divisível por 4 e NÃO for por 100, ele é bissexto direto
        print("É bissexto.")
else:
    # Se não for divisível por 4, já não é bissexto
    print("Não é bissexto.")