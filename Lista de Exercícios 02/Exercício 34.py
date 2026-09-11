'''Peça se o cliente é sócio da loja (S ou N) e informe o preço do ingresso: R$20 para sócios e R$40 para
não sócios.'''
socio = input("Você é sócio da loja? (S/N) ").upper()
if socio == "S":
    print(f"O valor do ingresso para sócio é R$ 20,00")
else:
    print(f"O valor do ingresso para não sócio é R$ 40,00")