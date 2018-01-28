def salarioHextra(salario, adicional, porcentagem, horas):
  if adicional == 0:
    salarioHoraExtra = (salario * porcentagem ) * horas
  else:  
    salarioHoraExtra = ((salario * adicional)* porcentagem ) * horas
  return salarioHoraExtra
  
def tabelaINSS(valor):
  if valor <= 1659.30:
    inss = valor * 0.08
  elif valor > 1659.30 and valor <= 2765.66:
    inss = valor * 0.09
  elif valor > 2765.66 and valor <= 5531.31:
    inss = valor * 0.11
  else:
    inss = 608.44
  return inss
  
def tabelaIRRF(valor):
  if valor < 1903.99:
    irrf = 0
  elif valor >= 1903.99 and valor < 2826.66:
    irrf = (valor * 0.075) - 142.80
  elif valor >= 2826.66 and valor < 3751.06:
    irrf = (valor * 0.15) - 354.80
  elif valor >= 3751.06 and valor < 4664.68:
    irrf = (valor * 0.225) - 636.13
  else: 
    irrf = (valor * 0.275) - 869.36
  return irrf
  
def periInsa(perico, insal, salBase):
  resp = 0.0
  if insal == '1':
    resp = 937 * 0.10
  elif insal == '2':
    resp = 187.40
  elif insal == '3':  
    resp = 937 * 0.40
  elif perico in "SIMsim":
    resp = salBase * 0.3
  return resp

salarioBase = float(input("Salario Base: "))
horaExtraNovembro = float(input("Hora extra até novembro: "))
porcentagemNovembro = float(input("%Novembro: "))
horaExtraDezembro = float(input("Hora extra até dezembro:"))
porcentagemDezembro = float(input("%Dezembro: "))
mesesNovembro = float(input("Número de meses até novembro: "))
mesesDezembro = float(input("Número de meses até dezembro: "))
numeroDeParcelas = float(input("Número de parcelas: "))
adicionalNoturno = float(input("Adicional Noturno: "))
dependentes = float(input("Nº dependentes: "))
periculosidade = input("Perico[S/N]: ")
instalubridade = input("Insalubridade Grau:\n1- Baixo  2- Médio  3- Alto >>>")

salarioHora = salarioBase / 220

salarioHoraExtraNovembro = salarioHextra(salarioHora, adicionalNoturno, porcentagemNovembro, horaExtraNovembro)

adr = (salarioHoraExtraNovembro / 305) * 60

bruto = salarioBase + salarioHextra(salarioHora, adicionalNoturno, porcentagemNovembro, horaExtraNovembro) + adr + periInsa(periculosidade, instalubridade, salarioBase)

liquido1 = ((bruto / 12) * mesesNovembro) / 2

print("\n===1ª Parcela===")
print ("salarioBase: {:.2f}".format(salarioBase))
print ("salarioHora: {:.2f}".format(salarioHora))
print ("salarioHoraExtra: {:.2f}".format(salarioHoraExtraNovembro))
print ("adr: {:.2f}".format(adr))
print ("bruto: {:.2f}".format(bruto))
print ("1ª Parcela: {:.2f}".format(liquido1))

salarioHoraExtraDezembro = salarioHextra(salarioHora, adicionalNoturno, porcentagemDezembro, horaExtraDezembro)

adr2 = (salarioHoraExtraDezembro / 305) * 60

bruto2 = salarioBase + salarioHoraExtraDezembro + adr2 + periInsa(periculosidade, instalubridade, salarioBase)

bruto3 = ((bruto2 / 12) * mesesDezembro)

inss1 = tabelaINSS(bruto3)

irrf1 = bruto3 - inss1 - (dependentes * 189.59)

irrf1 = tabelaIRRF(irrf1)

liquido = bruto3 - inss1 - irrf1 - liquido1

print("\n===2ª Parcela===")
print ("salarioHoraExtra: {:.2f}".format(salarioHoraExtraDezembro))
print ("adr: {:.2f}".format(adr2))
print("Burto: {}".format(bruto3))
print("(-)INSS: {:.2f}".format(inss1))
print("(-)IRRF: {:.2f}".format(irrf1))
print ("(-)1ª Parcela: {:.2f}".format(liquido1))
print("(=)2ª Parcela: {:.2f}".format(liquido))

