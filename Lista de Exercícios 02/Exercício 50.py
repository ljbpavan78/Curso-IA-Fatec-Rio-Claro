'''Peça o valor de uma compra e a forma de pagamento ("dinheiro" ou "cartao"). 
Se for dinheiro, aplique 10% de desconto sobre o valor. Se for cartão, pergunte o
número de parcelas; usando um if aninhado, se o número de parcelas for maior que
3, informe que haverá juros de 2% ao mês, senão informe que o pagamento será sem
juros. Exiba o valor final em cada situação.'''
valor = float(input("Digite o valor da compra: "))
forma_pagamento = input("Informe a forma de pagamento (dinheiro ou cartão): ").upper()
if forma_pagamento == "DINHEIRO":
    desconto = (valor * 10)/100
    valor_final = valor - desconto
    print(f"Você pagará com o desconto de 10% o valor de R$ {valor_final:.2f}")
else:
    parcelas = int(input("Em quantas parcelas? "))
    if parcelas>3:
        print("Haverá cobrança de juros de 2% ao mês")
        taxa = 0.02
        valor_final = valor * (1 + taxa) ** parcelas
        print(f"O valor final pago será de R$ {valor_final:.2f}")
    else:
        resultado = valor/3
        print("Pagamento será em 3x sem juros")
        print(f"Você pagará o valor de R$ {valor:.2f} em 3x de R$ {resultado:.2f} ")