"""Peça ao usuário quantos reais ele possui e converta esse valor para dólares,
considerando uma cotação fixa de 1 dólar = 5 reais (defina essa cotação
diretamente no código). Exiba o valor convertido."""
cotacao = 5.0
reais = float(input("Digite quantos reais você possui: ex.: 105.33: "))
dolares = reais / cotacao
print("O valor convertido para dólares é: US$ " + str(dolares))