def calcTempo(segundos):
    horas = segundos // 3600
    segundosRestantes = segundos % 3600
    minutos = segundosRestantes // 60
    resto = segundosRestantes % 60
    print("\nTempo estimado {} horas, {} minutos, {} segundos.".format(horas,minutos,resto))
    
