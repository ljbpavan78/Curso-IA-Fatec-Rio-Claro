'''Peça a nota final e o número de faltas de um aluno. Se o número de faltas for maior que
15, exiba "Reprovado por falta.". Caso contrário, use elif para classificar o aluno em A, B,
C ou D, conforme a nota (mesmas faixas do exercício 36).'''
nota = float(input("Digite a nota final do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))
if faltas > 15:
    print("Reprovado por falta.")
elif nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D")