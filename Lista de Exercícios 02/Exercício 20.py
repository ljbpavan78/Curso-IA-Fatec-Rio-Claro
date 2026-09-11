'''Peça ao usuário as medidas dos três lados de um triângulo (a, b, c) e exiba
True ou False para a expressão que verifica se eles podem formar um triângulo
válido: a + b > c and a + c > b and b + c > a'''
a = float(input("Digite a medida do primeiro lado do triângulo: "))
b = float(input("Digite a medida do segundo lado do triângulo: "))
c = float(input("Digite a medida do terceiro lado do triângulo: "))
resultado = a+b>c and a+c>b and b+c>a
print(f"As medidas {a}, {b} e {c} podem formar um triângulo? {resultado}")