import fun_Tempo

def calcVel(k):
    return k/8
  
i = 1
while i != 0:
    n = int(input("Velocidade contratada[(zero) para sair]: "))
    t = (float(input("Tamanho do arquivo em MegaBytes: ")))
    segundos = t / calcVel(n)
    fun_Tempo.calcTempo(segundos)
    print("Velocidade máxima de Download {} MB/s\n".format(calcVel(n)))
    i = n


    
