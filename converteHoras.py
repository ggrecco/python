segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
horas = segundos // 3600
segundosRestantes = segundos % 3600
minutos = segundosRestantes // 60
resto = segundosRestantes % 60
print("{} horas, {} minutos, {} segundos.".format(horas,minutos,resto))
