#test per lettura lettere con yautogui e pixel colorati
import pyautogui
import time
import random
def moveOn(x_min, x_max, y_min, y_max):
    # Genera coordinate casuali all'interno dell'intervallo
    x_coordinate = random.randint(x_min, x_max)
    y_coordinate = random.randint(y_min, y_max)
    # Sposta il mouse nella posizione casuale
    pyautogui.moveTo(x_coordinate, y_coordinate)
    # Genera un ritardo casuale tra 1 e 3 secondi
    ritardo_casuale = random.uniform(1, 3)
    time.sleep(ritardo_casuale)
#seleziona uno dei tre incarichi 
def check_rgb_conditions_yellow(coordinates):
    for coord in coordinates:
        x, y = coord
        r, g, b = pyautogui.pixel(x, y)

        # Verifica delle condizioni
        if r != 255 or b != 0:
            return False

    return True

def check_rgb_conditions_not_yellow(coordinates):
    for coord in coordinates:
        x, y = coord
        r, g, b = pyautogui.pixel(x, y)

        # Verifica delle condizioni invertite
        if r == 255 or b == 0:
            return False

    return True
    
def check_and_increment(result, label):
    print(f"Check lettera {label} su pixel giallo")
    if result:
        return 1
    else:
        return 0

# Esempio di coordinate (da sostituire con le tue)
A = [(1105, 413), (1109, 400), (1115, 375), (1126, 375), (1130, 400), (1138, 415), (1121, 404)]
L = [(1508, 376), (1509, 411), (1528, 412)]
esclamativo = [(1735, 375), (1735, 385), (1735, 412)]

negativoA = [(1120, 414), (1098, 387), (1141, 388)]
negativoL = [(1521, 396), (1493, 397)]

while 1:
    # Verifica delle condizioni e stampa del risultato
    # Positive checks (pixel giallo)
    i = 0
    i += check_and_increment(check_rgb_conditions_yellow(A), 'A')
    i += check_and_increment(check_rgb_conditions_yellow(L), 'L')
    i += check_and_increment(check_rgb_conditions_yellow(esclamativo), 'esclamativo')

    # Negative checks (non pixel giallo)
    i += check_and_increment(check_rgb_conditions_not_yellow(negativoA), 'negativo A')
    i += check_and_increment(check_rgb_conditions_not_yellow(negativoL), 'negativo L')

    if i == 5:
        print("Lettere trovate, aumento di livello riconosciuto...")
        moveOn(1608, 1766, 546, 640)
    else: 
        print("Lettere NON trovate")
    
    time.sleep(2)
    
   