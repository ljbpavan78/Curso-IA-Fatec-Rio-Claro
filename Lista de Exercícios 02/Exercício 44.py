'''Peça a idade e o sexo (M ou F) de uma pessoa. Usando ifs aninhados, exiba "Apto ao
serviço militar." apenas se a pessoa for do sexo masculino e maior de idade.'''
idade = int(input("Digite a idade da pessoa: "))
sexo = input("Digite o sexo da pessoa (M ou F): ")

if sexo == "M":
    if idade >= 18:
        print("Apto ao serviço militar.")
    else:
        print("Não apto ao serviço militar.")
else:
    print("Não apto ao serviço militar.")