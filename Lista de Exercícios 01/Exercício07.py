"""Peça ao usuário o ano de nascimento (use input()), converta para inteiro com int() e calcule a idade
aproximada da pessoa em 2026. Exiba o resultado concatenando texto e número (lembre-se de
converter o número de volta para str antes de concatenar)"""
anonascimento = int(input("Digite o ano de nascimento: "))
idadeem2026 = 2026 - anonascimento
print("A sua idade aproximada em 2026 será: " + str(idadeem2026) + " anos")