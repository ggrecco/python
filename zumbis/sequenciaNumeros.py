# imprima de 1 até numero digitado
n = int(input("Insira um número: "))
x = 0
if n > 0:
    while x <= n:
        print(x)
        x += 1
else:
    while x >= n:
        print(x)
        x -= 1
