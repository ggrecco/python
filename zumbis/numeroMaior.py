#ler 3 numeros e mostrar o maior deles
a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Terceiro: "))

if a >= b >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
