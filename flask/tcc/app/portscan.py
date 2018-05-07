import nmap
import os

#site pra teste -> 'testphp.vulnweb.com'
#site pra teste -> 'scanme.nmap.org'
def portScan(site):
    a = nmap.PortScanner()
    s = str(site)
    #scaneia as portas
    d = a.scan(s,'21,23,25,53,63,70,79,80,110,119', '-sV')
    #captura apenas o campo de ip e salva em um arquivo txt
    os.system("host " + s + " | awk '{print $4}' > ip.txt")

    arq = open('/home/ggrecco/Documentos/python/flask/tcc/ip.txt', 'r')
    ip = arq.read()
    b = ip.split("\n")
    ip = b[0]

    l = [21,23,25,53,63,70,79,80,110,119]#portas padrão que serão analisadas
    i = 0

    while i < len(l):
        j = d['scan'][ip]['tcp'][l[i]]['product']
        if j in '':
            pass
        else:
            print(j)
        i = i + 1
