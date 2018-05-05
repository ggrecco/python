d ={
'nmap':{
        'command_line': 'nmap -oX - -p 20-81 -sV testphp.vulnweb.com','scaninfo':{
            'tcp':{
                'method': 'connect', 'services': '20-81'
                }
            },
        'scanstats':{
            'downhosts': '0','elapsed': '11.32','timestr': 'Fri May  4 16:11:49 2018','totalhosts':'1','uphosts': '1'
            }
    },
'scan':{
        '176.28.50.165':{
            'addresses':{
                'ipv4': '176.28.50.165'
                },
            'hostnames': [{
                    'name': 'testphp.vulnweb.com', 'type': 'user'
                    },{
                    'name': 'rs202995.rs.hosteurope.de', 'type': 'PTR'
                }],
            'status':{
                'reason': 'conn-refused', 'state': 'up'
            },
            'tcp':{
                21:{
                    'conf': '10','cpe': 'cpe:/a:proftpd:proftpd:1.3.3e','extrainfo': '','name': 'ftp','product': 'ProFTPD','reason': 'syn-ack','state': 'open','version': '1.3.3e'
                },
                22:{
                    'conf': '10','cpe': 'cpe:/o:linux:linux_kernel','extrainfo': 'Ubuntu Linux; protocol 2.0','name': 'ssh', 'product': 'OpenSSH','reason': 'syn-ack','state': 'open','version': '5.3p1 Debian 3ubuntu7.1'
                },
                25:{
                    'conf': '10','cpe': 'cpe:/a:postfix:postfix','extrainfo': '','name': 'smtp','product': 'Postfix smtpd','reason': 'syn-ack','state': 'open','version': ''
                },
                53:{
                    'conf': '10','cpe': 'cpe:/a:isc:bind:none','extrainfo': '','name': 'domain','product': 'ISC BIND','reason': 'syn-ack','state': 'open','version': 'none'
                },
                80:{
                    'conf': '10','cpe': 'cpe:/a:igor_sysoev:nginx:1.4.1', 'extrainfo': '','name': 'http','product': 'nginx','reason': 'syn-ack','state': 'open','version': '1.4.1'
                }
            },
            'vendor': {

            }
        }
    }
}
# import nmap
# a = nmap.PortScanner()
# d = a.scan('testphp.vulnweb.com','20-81', '-sV')
# d = a.scan('testphp.vulnweb.com','21,23,25,53,63,70,79,80,110,119', '-sV')
 # d['scan']['176.28.50.165']['tcp'][80]['product']
# l = [21,23,25,53,63,70,79,80,110,119]
# i = 0
# while i < len(l):
#     j = l[i]
#     d['scan']['176.28.50.165']['tcp'][j]['product']
#     i = i + 1
