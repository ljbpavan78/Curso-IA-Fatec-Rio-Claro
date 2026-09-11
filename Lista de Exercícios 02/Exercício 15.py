'''Peça ao usuário a média final e a frequencia (%) de um aluno. Exiba True ou
False para a expressão que representa a aprovação: media >=6 and frequencia
>=75'''
mediafinal = float(input("Digite a média final do aluno (0 a 10): "))
frequencia = float(input("Digite a frequência do aluno (0 a 100): "))
aprovação = (mediafinal >=6 and frequencia >=75)
print(f"O aluno foi aprovado? {aprovação}")