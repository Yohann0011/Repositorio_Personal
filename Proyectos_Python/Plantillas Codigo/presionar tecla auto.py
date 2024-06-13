#pip install necesarios
#pip install pyautogui
"""
========================================================================
-------------------------| IMPORTACIONES |------------------------------
========================================================================
"""
import pyautogui
import time

"""
========================================================================
-----------------------| VARIABLES GLOBALES |---------------------------
========================================================================
"""


"""
========================================================================
---------------------------| FUNCIONES |--------------------------------
========================================================================
"""
def simulate_key_press(key='f6', interval=2):
    try:
        while True:
            pyautogui.press(key)
            print(f"Presionada la tecla '{key}'")
            time.sleep(interval)
    except KeyboardInterrupt: #control + c para parar
        print("Simulación detenida por el usuario.")
"""
========================================================================
-----------------------------| LÓGICA |---------------------------------
========================================================================
"""

if __name__ == "__main__":
    simulate_key_press('f6', 2)  # Cambia 'a' y 5 por la tecla y el intervalo que desees




