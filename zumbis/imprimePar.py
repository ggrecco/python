#imprimir numeors pares entre 0 e um numero fornecido
n = int(input("Digite um número: "))
x = 0
while x <= n:
    if x % 2 == 0:
        print(x, end=" ")
    x += 1
    
