''' Peça ao usuário uma senha e compare com a senha correta "fatec123" definida
diretamente no código, usando ==. Exiba o resultado da comparação'''
senha = input("Digite a senha: ")
resultado = senha == "fatec123"
print(f"A senha digitada é: {resultado}")