'''Peça o valor de uma compra e aplique desconto progressivo usando elif: até R$50 sem
desconto; até R$200, 5% de desconto; até R$500, 10% de desconto; acima de R$500, 15% de 
desconto. Exiba o valor final da compra.'''
compra = float(input("Digite o valor da compra: R$ "))
if compra <= 50:
    desconto = 0
elif compra <= 200:
    desconto = 0.05
elif compra <= 500:
    desconto = 0.10
else:
    desconto = 0.15
valor_final = compra * (1 - desconto)
print(f"Valor final da compra com desconto: R$ {valor_final:.2f}")