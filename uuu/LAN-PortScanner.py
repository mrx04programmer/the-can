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
import socket, os
sh = os.system
smbports = [139, 137, 138, 445, 631]
httpports = [80, 8080, 8090]
oports = [22, 2222, 2121, 1234, 4444, 21, 9999, 9090]
dataports = [3306, 8027, 8000, 88]
savesports = [443, 442, 8443, 8343, 2432]

def clear():
    sh("clear")

def main():
    def banner(ip):
        clear()
        print(f"{W}-"*40)
        print(f"{O}[*] {W}Escaneo iniciado en : {G}{ip}")
        print(f"{W}-"*40)
        
    def start(ip):
        banner(ip)
        hostbyname = socket.gethostbyname(ip)
        try:
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((ip, port))
                if (result == 0):
                    print(f"{G}[+]{W} Se encontro el puerto {port} ")
                    if (port in smbports):
                        print(f"{R}[+]{W} SMB Ataque vulnerable !")
                    elif (port in httpports):
                        print(f"{R}[+]{W} HTTP Ataque vulnerable !")
                    elif (port in oports):
                        print(f"{R}[+]{W} PointerSever Ataque vulnerable !")
                    elif (port in dataports):
                        print(f"{R}[+]{W} SQL-Injection Ataque vulnerable !")
                    elif (port in savesports):
                        print(f"{B}[o]{W} Puerto muy seguro")
                    s.close()
            print(f"{G}{datetime.now()} {W} Escaneo termiado exitosamente ")
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
            ip = input(f"{G}IP a escanear:{W}")
            start(ip)
        except Exception:
            print(f"{R}IP Invalida o sin conexión, {C}Bye Bye.")
    run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{R}Error causado por {O}{e}")