import platform
import subprocess

def hacer_ping(host):
    if platform.system().lower() == "windows":
        comando = ["ping", "-n", "1", "-w", "1000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "1", host]
    try:
        resultado = subprocess.run(comando, stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, timeout=5)
        return resultado.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False

host = input("Host o IP a probar: ").strip()
if hacer_ping(host):
    print(host, "responde")
else:
    print(host, "no responde")
