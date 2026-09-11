''' Peça ao usuário um ano e exiba True ou False verificando se o ano é bissexto,
usando uma única expressão lógica: ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0).'''
ano = int(input("Digite o ano desejado para verificar se é bissexto: "))
teste = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
print(f"O ano de {ano} é ou não é bissexto? {teste} ")