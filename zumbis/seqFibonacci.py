#Sequencia de fibonacci
n = int(input("N: "))
a, b = 1,1
k = 1
while k < n - 1:
    a, b = b , a+b
    k += 1
print("Fib({}) = {}".format(n,b))
