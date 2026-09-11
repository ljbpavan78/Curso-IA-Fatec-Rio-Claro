'''Peça a temperatura e a umidade do ar. Usando ifs aninhados, verifique primeiro
se a temperatura é maior que 30 graus; se for, verifique dentro desse if se a 
umidade é menor que 30%, exibindo "Alerta de incêndio!" nesse caso, ou "Calor,
mas sem risco de incêndio." caso contrário'''
temperatura = float(input("Digite a temperatura atual: "))
umidade_do_ar= float(input("Digite a umidade do ar: "))
if temperatura >30:
    if umidade_do_ar<30:
        print("Alerta de Incêndio")
    else:
        print("Calor, mas sem risco de incêndio")