"""Peça ao usuário seu nome e sua idade atual. Calcule e exiba em que ano
ele completará 100 anos, concatenando texto e números na mensagem final."""
nome = input("Digite seu nome: ")
idade = int(input("Quantos anos você tem? "))
anoatual = 2026
anoquecompleta100 = anoatual + (100 - idade)
print(nome + ", você completará 100 anos no ano de " + str(anoquecompleta100))