sexo = input("Digite o sexo (M ou F): ")

# Criamos uma única expressão lógica (usando .upper() para aceitar maiúsculo ou minúsculo)
resultado = sexo.upper() == "M" or sexo.upper() == "F"

# Exibimos o resultado booleano (True ou False)
print(f"O valor digitado é válido? {resultado}")