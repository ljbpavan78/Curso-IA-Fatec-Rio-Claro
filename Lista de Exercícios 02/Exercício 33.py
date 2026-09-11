'''Peça o valor de uma compra e informe se ela terá desconto de 10% (para compras acima de
R$100) ou se não terá desconto, exibindo o valor final da compra em cada caso.'''
compra = float(input("Digite o valor da compra R$ "))
if compra > 100:
    resultado = compra * 0.10
    total = compra - resultado
    print(f"Você terá o desconto de 10%. Pagará por sua compra o valor de R$ {total:.2f}")
else:
    print(f"Você não terá desconto. Pagará por sua compra o valor de R$ {compra:.2f}")