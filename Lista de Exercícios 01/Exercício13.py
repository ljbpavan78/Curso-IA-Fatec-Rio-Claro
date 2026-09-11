"""Peça ao usuário a nota de duas provas (numeros com casas decimais) e calcule
a média aritmética entre elas, exibindo o resultado final."""
prova1 = float(input("Digite a nota da primeira prova (ex.: 7.5): "))
prova2 = float(input("Digite a nota da segunda prova (ex.: 8.0): "))
media = (prova1 + prova2) / 2
print("A média aritmética das duas provas é: " +str(media))