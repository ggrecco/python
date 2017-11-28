n = int(input("digite a largura: "))
j = int(input("digite a altura: "))
x = 1
while x <= j:
    print("#", end="")
    coluna = 0
    while coluna < (n - 2):
        if x == 1 or x == j:
            print("#", end="")
        else:
            print(end=" ")
        coluna = coluna + 1
    print("#")
    x = x + 1
