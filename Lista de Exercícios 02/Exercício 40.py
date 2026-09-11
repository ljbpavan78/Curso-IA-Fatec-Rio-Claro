'''Peça a quantidade de minutos utilizados no plano de celular (como no exemplo visto em
aula) e calcule o valor a pagar usando elif com 4 faixas de preço: até 100 minutos R$0,25; 
até 300 minutos R$0,20; até 500 minutos R$0,15; acima de 500 minutos R$0,10.'''

minutos = int(input("Quantidade de minutos utilizados: "))

if minutos <= 100:
    valor_por_minuto = 0.25
elif minutos <= 300:
    valor_por_minuto = 0.20
elif minutos <= 500:
    valor_por_minuto = 0.15
else:
    valor_por_minuto = 0.10

valor_a_pagar = minutos * valor_por_minuto
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")