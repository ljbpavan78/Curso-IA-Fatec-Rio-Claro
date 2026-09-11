from vlibras_translate import Translate

# Inicializa o tradutor do VLibras
translator = Translate()

texto_portugues = "O menino gosta de jogar futebol com os amigos."

# Realiza a tradução para a estrutura de Glosa
glosa_libras = translator.translate(texto_portugues)

print(f"Texto original: {texto_portugues}")
print(f"Em Libras (Glosa): {glosa_libras}")
