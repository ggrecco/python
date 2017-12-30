'''
usuário informa o tamanho em metros quadrados a ser pintado
Cada litro de tinta pinta 3 metros quadrados e a tinta
é vendida em latas de 18 litros, que custam R$ 80,00
devolver para o usuário o numero de latas necessárias
e o preço total.
Somente são vendidas nº inteiro de latas
'''
m = float(input("Metros²: "))
if m % 54 != 0:#1 lata tem 18 litros que pintam o total de 54 metros
    latas = int(m / 54) + 1
else:
    latas = m / 54

valor = latas * 80

print("{} Latas custando R$ {:.2f}".format(latas,valor))
