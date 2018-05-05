import nmap


a = nmap.PortScanner()

#testphp.vulnweb.com site deverá ser passado por parametro como string
d = a.scan('testphp.vulnweb.com','21,23,25,53,63,70,79,80,110,119', '-sV')


l = [21,23,25,53,63,70,79,80,110,119]#portas padrão que serão analisadas
i = 0

while i < len(l):
    j = l[i]
    d['scan']['176.28.50.165']['tcp'][j]['product']
    i = i + 1
