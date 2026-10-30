import socket

PUERTOS = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
           80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
           3306: "MySQL", 3389: "RDP"}

def puerto_abierto(host, puerto, espera=1.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(espera)
    try:
        return s.connect_ex((host, puerto)) == 0
    finally:
        s.close()

host = input("Host o IP a escanear: ").strip()
try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("No se pudo resolver", host)
    raise SystemExit(1)

print("Escaneando", ip)
for puerto, servicio in PUERTOS.items():
    estado = "ABIERTO" if puerto_abierto(ip, puerto) else "cerrado"
    print("{:>5} {:<8} {}".format(puerto, servicio, estado))
