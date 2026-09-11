'''Peça uma senha e informe "Acesso liberado." ou "Acesso negado.", comparando com a senha
correta definida no código.'''
senhacorreta = "fatec123"
senha = input("Digite a senha: ")

if senha == senhacorreta:
    print("Acesso liberado.")
else:
    print("Acesso negado.")