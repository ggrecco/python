opcao = True
while opcao is True:
  vt = float(input("Custo mensal do VT:"))
  diasUteis = float(input("Dias uteis:"))
  feriados = float(input("Feriados:"))
  horaExtra = float(input("Número de Horas Extra:"))
  valorHoraExtra = float(input("% Extra:"))
  dependentes = float(input("Dependentes:"))
  salarioBase = float(input("Salario Normal:"))
  insalubridade = float(input("Insalubridade:"))
  perico = float(input("Perico: "))

  #adiciona
  #dias trabalhados
  diasTrabalhados = diasUteis + feriados
  #valor da hora trabalhada
  valorHora = salarioBase / 220 
  #Salario Extra
  salarioExtra = valorHora * horaExtra * valorHoraExtra
  #salario ADR
  salarioADR = (salarioExtra / diasUteis) * feriados 
  #Horas Trabalhadas
  horasT = (diasTrabalhados * 220) / 30
  #salario Normal
  salarioNormal = horasT * valorHora
  #periculosidade
  insper = perico + insalubridade
  #bruto
  bruto = salarioNormal + salarioADR + salarioExtra + insper


  #(--------------------------------------------------------------------)
  #subtrai
  #inss
  if bruto <= 1659.30:
    inss = bruto * 0.08
  elif bruto > 1659.30 and bruto <= 2765.66:
    inss = bruto * 0.09
  elif bruto >= 2765.67 and bruto <= 5531.31:
    inss = bruto * 0.11
  else:
    inss = 608.44

  #Imposto de Renda
  irrf = bruto - inss - (189.59 * dependentes)

  if irrf <= 1903.98:
    irrf = 0
  elif irrf > 1903.98 and irrf <= 2826.65:
    irrf = (irrf * 0.075) - 142.80
  elif irrf > 2826.65 and irrf <= 3751.05:
    irrf = (irrf * 0.15) - 354.80
  elif irrf > 3751.05 and irrf <= 4664.68:
    irrf = ( irrf * 0.225) - 636.13
  elif irrf > 4664.68:
    irrf = (irrf * 0.275) - 869.36

  #vale transporte
  novoVT = 0
  if diasTrabalhados <= 30:
    novoVT = salarioBase * 0.06
    novoVT = (diasTrabalhados * novoVT) / 30
  #verifica VT menor
  if novoVT < vt: 
    vt = novoVT 

  #salarioFamilia
  salarioFamilia = 0
  if salarioBase <= 859.88:
    salarioFamilia =  (dependentes * 44.09 * diasTrabalhados) / 30
  elif salarioBase <= 1292.43:
    salarioFamilia =  (dependentes * 31.07 * diasTrabalhados) / 30

  liquido = bruto - inss -irrf - vt + salarioFamilia

  print("")
  print("===ACRÉSCIMOS===")
  print("Nº de Horas: {:.2f}".format(horasT))
  print("Hora Extra: R$ {:.2f}".format(horaExtra))
  print("Salario Normal: R$ {:.2f}".format(salarioNormal))
  print("salarioExtra: R$ {:.2f}".format(salarioExtra))
  print("salarioADR: R$ {:.2f}".format(salarioADR))
  print("Ins/PER: {:.2f}".format(insper))
  print("Bruto: R$ {:.2f}".format(bruto))
  print("\n===DESCONTOS===")
  print("inss: R$ {:.2f}".format(inss))
  print("Vale Transporte: R$ {:.2f}".format(vt))
  print("IRRF: {:.2f}".format(irrf))
  print("salarioFamilia: {:.2f}".format(salarioFamilia))
  print("Liquido: {:.2f}".format(liquido))
  opcao = input("Ddeseja Continuar[S/N]:")
  if opcao in "Nn":
    opcao = False
  else:
    opcao = True
