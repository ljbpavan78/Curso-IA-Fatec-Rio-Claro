'''Peça duas notas e a frequência (%) de um aluno. Primeiro verifique, com um if,
se a frequência é maior ou igual a 75%. Dentro desse if, verifique a média das 
notas: se for maior ou igual a 6, exiba "Aprovado.", senão exiba "Reprovado por
nota.". Caso a frequência seja menor que 75%, exiba "Reprovado por falta."'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
if nota1<0 or nota1>10 or nota2<0 or nota2>10:
    print("Digite a nota entre 0 e 10")
else:
    frequencia = float(input("Digite a frequencia do aluno: "))
    if frequencia<0 or frequencia>100:
        print("Digite a frequencia do aluno entre 0 e 100")
    else:
        
        if frequencia>=75:
            media = (nota1+nota2)/2
            if media>=6:
                print("Aprovado")
            else:
                print("Reprovado por nota")
        else:
            print("Reprovado por falta")