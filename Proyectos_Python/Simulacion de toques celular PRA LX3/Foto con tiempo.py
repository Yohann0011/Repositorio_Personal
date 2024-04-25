import subprocess
import time

# Esperar 3 segundos
time.sleep(3)

# Lista de coordenadas de toques
coordinates = [(350, 1260),]  # Modifica estas coordenadas según tus necesidades

# Itera sobre las coordenadas y ejecuta un toque en cada una
for x, y in coordinates:
    adb_command = f'adb shell input tap {x} {y}'
    subprocess.run(adb_command, shell=True)