j = int(input("Qual tabuada deseja visualizar? >>> "))
t = int(input("até qual número deseja imprimir? >>>"))
k = 0
lista = []
for i in range(0,((j*t)+1),j):
    lista.append(i)

#print(lista)

while k <= t: 
    print("{:2} X {:2} = {:2}".format(k,j,lista[k]))
    k = k + 1

