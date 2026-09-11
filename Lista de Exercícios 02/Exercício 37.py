'''Peça a idade do usuário e classifique a faixa etária usando elif: criança 
(menor que 12), adolescente (menor que 18), adulto (menor que 60) e idoso 
(60 ou mais)'''
idade = int(input("Digite a idade: "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")