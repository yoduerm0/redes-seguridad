import socket
import ssl
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

dominio = input("Dominio (sin https://): ").strip()
inicio = time.perf_counter()
try:
    with urllib.request.urlopen("https://" + dominio, timeout=5) as r:
        codigo = r.status
except urllib.error.HTTPError as e:
    codigo = e.code
except OSError as e:
    print("No se pudo conectar:", e)
    raise SystemExit(1)

ms = (time.perf_counter() - inicio) * 1000
print("Código HTTP:", codigo)
print("Tiempo de respuesta: {:.0f} ms".format(ms))

contexto = ssl.create_default_context()
with socket.create_connection((dominio, 443), timeout=5) as sock:
    with contexto.wrap_socket(sock, server_hostname=dominio) as s:
        cert = s.getpeercert()

vence = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
vence = vence.replace(tzinfo=timezone.utc)
dias = (vence - datetime.now(timezone.utc)).days
print("El certificado vence en", dias, "días")
