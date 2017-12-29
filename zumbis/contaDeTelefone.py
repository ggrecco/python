minutos = float(input("Minutos de ligação: "))
if minutos < 200:
    print("Sua conta será: R$ {:.2f}".format(minutos * 0.2))
elif minutos >= 200 and minutos < 400:
    print("Sua conta será: R$ {:.2f}".format(minutos * 0.18))
elif minutos >= 400:
    print("Sua conta será: {:.2f}".format(minutos * 0.15))
else:
    print("O valor não pode ser calculado")
