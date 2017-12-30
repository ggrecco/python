#Calcula fatorial de número digitado pelo usuário
n = 1
fat = 1
limite = int(input("Fatorial de: "))
while n <= limite:
    fat = fat * n
    n = n + 1
print("O fatorial de {} é {}".format(limite,fat))
