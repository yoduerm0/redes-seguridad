import socket
import statistics
import time

host = input("Host: ").strip()
puerto = int(input("Puerto (ej. 443): "))
intentos = 5
tiempos = []
perdidos = 0

for i in range(intentos):
    inicio = time.perf_counter()
    try:
        with socket.create_connection((host, puerto), timeout=2):
            ms = (time.perf_counter() - inicio) * 1000
            tiempos.append(ms)
            print("Intento {}: {:.1f} ms".format(i + 1, ms))
    except OSError:
        perdidos += 1
        print("Intento {}: sin respuesta".format(i + 1))
    time.sleep(0.5)

if tiempos:
    print("Mín {:.1f} ms  Máx {:.1f} ms  Prom {:.1f} ms".format(
        min(tiempos), max(tiempos), statistics.mean(tiempos)))
print("Pérdida: {:.0f}%".format(perdidos / intentos * 100))
