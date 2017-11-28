import math
xa = float(input("Digite o Xa"))
ya = float(input("Digite o ya"))
xb = float(input("Digite o xb"))
yb = float(input("Digite o yb"))
distancia = math.sqrt((xb - xa)**2 + (yb - ya)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
