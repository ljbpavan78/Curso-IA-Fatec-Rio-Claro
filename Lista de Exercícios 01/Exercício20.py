"""Crie um pequeno "cadastro de aluno": peça nome, idade e a nota final do aluno
(número decimal). Depois exiba um resumo com tdas as informações organizadas,
cada uma em uma linha, no formato:
Nome:
Idade:
Nota final:"""
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
notafinal = float(input("Digite a nota final do aluno: (ex.: 8.5): "))

print("Nome: " + nome)
print("Idade: " + str(idade))
print("Nota final: " + str(notafinal))