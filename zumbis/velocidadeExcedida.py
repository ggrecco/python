velocidade = int(input("Velocidade do carro: "))
if velocidade > 110:
    multa = (velocidade - 110) * 5    
    print("Você foi mulado em R$ {}".format(multa))
else:
    print("Parabéns você está dentro do limite de velocidade!")
