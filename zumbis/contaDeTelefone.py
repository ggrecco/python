minutos = float(input("Minutos de ligação: "))
'''
#meu codigo
if minutos < 200:
    print("Sua conta será: R$ {:.2f}".format(minutos * 0.2))
elif minutos >= 200 and minutos < 400:
    print("Sua conta será: R$ {:.2f}".format(minutos * 0.18))
elif minutos >= 400 and minutos < 800:
    print("Sua conta será: {:.2f}".format(minutos * 0.15))
elif minutos >= 800:
    print("Sua conta sserá: {:.2f}".format(minutos * 0.08))
else:
    print("O valor não pode ser calculado")
'''
#Profissional
if minutos < 200:
    preco = 0.20
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08
print("Conta telefônica: R$ {:.2f}".format(minutos * preco))
