## LAN - Port Scanner
# Author: Mrx04programmer
W = '\033[1;37m' # Default
WR = '\033[37m' # gray
R = '\033[1;31m'  # red
G = '\033[3;32m'  # green
GG = '\033[1;32m'  # green2
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
import socket, os,sys, platform
sh = os.system

db = [5900, 3283, 22]

def clear():
    sh("clear")

def main():
    def banner(ip):
        clear()
        print(f"{W}-"*40)
        print(f"{O}[*] {W}Buscando Vulnerabilidades RDP o Similares{G}")
        print(f"{G}[*] {W}Objetivo: {P}{ip}")
        print(f"{W}-"*40)
        
    def start(ip):
        w = 0
        banner(ip)
        hostbyname = socket.gethostbyname(ip)
        try:
            while (w < int(len(db))):
                port = db[w]
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((ip, port))
                if (result == 0):
                    print(f"{G}[+]{W} El dispositivo {ip} se encontro vulnerable en el puerto {port}")
                    if (port == 5900):
                        print(f"{O}[!] {W}El dispositivo cuenta con control de pantalla")
                    if(port == 3283):
                        print(f"{O}[!] {W}El dispositivo envia informes a terceros o datos adicionales a los comunes.")
                    if (port == 22):
                        print(f"{O}[!] {W}El dispositivo cuenta con terminal remota.")
                else:
                    pl = platform.platform()
                    if "indow" in pl:
                        ping = sh(f"ping -n 1 {ip} > pings.tmp")
                    else:
                        ping = sh(f"ping -c 1 {ip} > /dev/null")
                    if ping != 0:
                        print(f"{R}[-] {W}El dispositivo no esta disponible o no se encuentra en linea")
                        exit()
                    else:
                        print(f"{R}[-]{W} El dispositivo no es vulnerable en el puerto {port}")
                w += 1
                s.close()
        except KeyboardInterrupt:
            print(f"{G}Bye bye.")
        except socket.gaierror:
            print(f"{R}El dispositivo {ip} no esta disponible o no tiene internet.")
            sys.exit()
        except socket.error:
            print(f"{R}Tu dispositivo local no responde !")
            sys.exit()
    def run():
        try:
            ip = sys.argv[1]
            start(ip)
        except Exception as e:
            print(f"{R}[-] {W}Error causado por :{e}.\n{G}Ejecuta: {W}{sys.argv[0]} <ip>")
    run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{R}Error causado por {O}{e}")
