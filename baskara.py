import math
a = int(input("Digite o parâmetreo a"))
b = int(input("Digite o parâmetreo b"))
c = int(input("Digite o parâmetreo c"))
delta = (b**2) - (4*a*c)
if delta < 0:
  print("esta equação não possui raízes reais")
else:
    rSoma = ((-b) + math.sqrt(delta))/2*a
    rSub = ((-b) - math.sqrt(delta))/2*a
    if rSoma > rSub:
      print("as raízes da equação são {} e {}".format(rSub,rSoma))
    if rSoma < rSub:
      print("as raízes da equação são {} e {}".format(rSoma,rSub))
    if rSoma == rSub:
      print("a raiz desta equação é {}".format(rSoma))
<<<<<<< HEAD
=======
#comentário para testar o git
>>>>>>> 010529b5fed1e8d341b34e8387002d2482b1b88f
