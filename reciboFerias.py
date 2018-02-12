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
  
def venda(valor):
  vendas = (valor * 20) / 30
  return vendas
  
def salarioHextra(salario, adicional, porcentagem, horas):
  if adicional == 0:
    salarioHoraExtra = (salario * porcentagem ) * horas
  else:  
    salarioHoraExtra = ((salario *  porcentagem) * adicional ) * horas
  return salarioHoraExtra
  
salarioBase = float(input("Salario base: "))
periculosidade = input("Perico[S/N]: ")
instalubridade = input("Insalubridade Grau:\n1- Baixo  2- Médio  3- Alto >>>")
vendaFerias = input("Venda de 1/3 das férias[S/N]: ")
dependentes = int(input("Nº de dependentes: "))
adicionalNoturno = float(input("Adicional Noturno(%1.2%): "))
horaExtraNovembro = float(input("Hora extra: "))
porcentagemNovembro = float(input("%: "))

abono = 0

salarioHora = salarioBase / 220

salarioHoraExtraFerias = salarioHextra(salarioHora, adicionalNoturno, porcentagemNovembro, horaExtraNovembro)

adr = (salarioHoraExtraFerias / 305) * 60

pericoinsalu = periInsa(periculosidade, instalubridade, salarioBase)

tercoFerias = (salarioBase + salarioHoraExtraFerias + adr + pericoinsalu) / 3

bruto = salarioBase + pericoinsalu + tercoFerias + adr + salarioHoraExtraFerias

if vendaFerias in "SIMsim":
  bruto = venda(bruto)
  abono = bruto / 2

inss1 = tabelaINSS(bruto)

irrf1 = bruto - inss1 - (dependentes * 189.59)
irrf1 = tabelaIRRF(irrf1)

liquido = bruto - inss1 - irrf1 + abono



print("\nPer/Ins: {:.2f}".format(pericoinsalu))
print("1/3 férias: {:.2f}".format(tercoFerias))
print("\n===RECIBO FÉRIAS===\nBruto: {:.2f}".format(bruto))
print("(-)INSS: {:.2f}".format(inss1))
print("(-)IRRF: {:.2f}".format(irrf1))
print("(+)Abono: {:.2f}".format(abono))
print("(=)Liquido: {:.2f}".format(liquido))
print("\n===Horas Extras===")
print("Salario Extra: {:.2f}".format(salarioHoraExtraFerias))
print("Salario Extra: {:.2f}".format(adr))
