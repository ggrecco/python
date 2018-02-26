#imprime tabuada de 1 a 10
tabuada = 1
while tabuada <= 10:
    n = 1
    print("\nTabuada {:2}".format(tabuada))
    while n <= 10:
        print("{:2} X {:2} = {:2}".format(tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada +1
