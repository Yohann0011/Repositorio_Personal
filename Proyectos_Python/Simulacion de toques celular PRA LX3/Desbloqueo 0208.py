import subprocess

# Realizar un deslizamiento desde (400, 1000) a (400, 400)
swipe_command = 'adb shell input swipe 400 1000 400 400'
subprocess.run(swipe_command, shell=True)

# Lista de coordenadas de toques
coordinates = [(350, 1320), (350, 1000), (350, 1320), (350, 1215)]  # Modifica estas coordenadas según tus necesidades

# Itera sobre las coordenadas y ejecuta un toque en cada una
for x, y in coordinates:
    adb_command = f'adb shell input tap {x} {y}'
    subprocess.run(adb_command, shell=True)
