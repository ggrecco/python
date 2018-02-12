#imprimir os 10 primeiros multiplos de 3
'''
#usuário informando número
n = int(input("Digite um número: "))
x = 0
while x < n:
    if x % 3 == 0:
        print(x)
    x += 1
'''
#usuário não informa
x = 1
print(x)
while x < 10:
    print(x * 3)
    x += 1
