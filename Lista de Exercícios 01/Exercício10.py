"""Peça ao usuário o preço de um produto (número com casas decimais) e a 
quantidade de unidades desejadas (número inteiro). Calcule o valor total da 
compra e exiba o resultado."""
preco = float(input("Digite o preço do produto (ex: 10.50): "))
quantidade = int(input("Digite a quantidade de unidades desejadas: "))
valortotal = preco * quantidade
print("O valor total da compra é: R$ " + str(valortotal))