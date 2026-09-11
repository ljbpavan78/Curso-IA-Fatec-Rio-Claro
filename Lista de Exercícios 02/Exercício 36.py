'''Peça uma nota de 0 a 10 e classifique o conceito do aluno usando elif: 
A (nota >= 9), B (nota >= 7), C (nota >= 5) e D (nota < 5).'''
nota = float(input("Digite a nota do aluno: "))
if nota >= 9:
    print("O aluno obteve nota A")
elif nota >=7:
    print("O aluno obteve nota B")
elif nota >=5:
    print("O aluno obteve nota C")
else:
    print("O aluno obteve nota D")