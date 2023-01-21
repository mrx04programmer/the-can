## LAN - IP Scanner
# Author: Mrx04programmer
# Github : https://github.com/mrx04programmer
import os, platform
sh = os.system

W = '\033[1;37m' # Default
WR = '\033[37m' # gray
R = '\033[1;31m'  # red
G = '\033[3;32m'  # green
GG = '\033[1;32m'  # green2
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan

plataforma = platform.platform()
print(f"{O}Posibles IP:{W}")
if ("Window" in plataforma):
    sh("ipconfig | findstr IPv4 && ipconfig")
else:
    sh("ip -4 addr show | grep 'inet' | awk '{print $2}'")
ip = input(f"{W}IP del Gateway o Router{O}({W}ej: {R}10.20.30.1{O}) {W}>> {C}")
rang = input(f"{W}Rango a escanear {O}({W}Default: {R}24{O}){W} >>{C}")

ipformat = ip[0:-1]
if rang == '':
    rang = 24
else:
    rang = int(rang)
#print(plataforma)
try:
    w = 1
    while (w<rang):
        if ("Window" in plataforma):
            verify = sh(f"ping -n 1 {ipformat}{w} > pings.log")
        else:
            verify = sh(f"ping -c 1 {ipformat}{w} > /dev/null")
        
        if verify == 0:
            print(f"{G}[+] {W}Dispositivo encontrado {C}{ipformat}{w}")
        else:
            pass
        w += 1
except Exception as e:
    print(f"{R}[-] {W}No se logro realizar el escaneo y su causa es {R}{e}")