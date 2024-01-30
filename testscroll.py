import pyautogui
import time
import random

def clickOn(x_min, x_max, y_min, y_max):
    # Genera coordinate casuali all'interno dell'intervallo
    x_coordinate = random.randint(x_min, x_max)
    y_coordinate = random.randint(y_min, y_max)
    # Sposta il mouse nella posizione casuale
    pyautogui.click(x_coordinate, y_coordinate)
    # Genera un ritardo casuale tra 1 e 3 secondi
    ritardo_casuale = random.uniform(0.2, 0.34)
    time.sleep(ritardo_casuale)

def moveOn(x_min, x_max, y_min, y_max):
    # Genera coordinate casuali all'interno dell'intervallo
    x_coordinate = random.randint(x_min, x_max)
    y_coordinate = random.randint(y_min, y_max)
    # Sposta il mouse nella posizione casuale
    pyautogui.moveTo(x_coordinate, y_coordinate)
    # Genera un ritardo casuale tra 1 e 3 secondi
    ritardo_casuale = random.uniform(1, 3)
    time.sleep(ritardo_casuale)

def clickAndDragUpFromCenter():
    # Calcola le coordinate del centro dello schermo
    centro_x, centro_y = pyautogui.size()[0] // 2, pyautogui.size()[1] // 2

    # Muove casualmente nel rettangolo vicino al centro dello schermo
    moveOn(centro_x - 50, centro_x + 50, centro_y - 50, centro_y + 50)

    # Tieni premuto il pulsante del mouse
    pyautogui.mouseDown()

    # Genera nuove coordinate per il trascinamento
    x_finale = random.randint(centro_x - 50, centro_x + 50)
    y_finale = random.randint(centro_y - 150, centro_y - 100)  # Sposta leggermente verso l'alto

    # Muovi il cursore al punto finale del trascinamento
    pyautogui.moveTo(x_finale, y_finale, duration=1)

    # Rilascia il pulsante del mouse
    pyautogui.mouseUp()

def clickAndDragDownFromCenter():
    # Calcola le coordinate del centro dello schermo
    centro_x, centro_y = pyautogui.size()[0] // 2, pyautogui.size()[1] // 2

    # Muove casualmente nel rettangolo vicino al centro dello schermo
    moveOn(centro_x - 50, centro_x + 50, centro_y - 50, centro_y + 50)

    # Tieni premuto il pulsante del mouse
    pyautogui.mouseDown()

    # Genera nuove coordinate per il trascinamento
    x_finale = random.randint(centro_x - 50, centro_x + 50)
    y_finale = random.randint(centro_y + 100, centro_y + 150)  # Sposta leggermente verso il basso

    # Muovi il cursore al punto finale del trascinamento
    pyautogui.moveTo(x_finale, y_finale, duration=1)

    # Rilascia il pulsante del mouse
    pyautogui.mouseUp()

# Calcola le coordinate del centro dello schermo all'inizio del programma
centro_x, centro_y = pyautogui.size()[0] // 2, pyautogui.size()[1] // 2

# Esegui l'azione di clic e trascinamento in modo continuo
while True:
    clickAndDragUpFromCenter()
    time.sleep(2)  # Aggiungi un ritardo tra le azioni se necessario
    clickAndDragDownFromCenter()
    time.sleep(2)  # Aggiungi un ritardo tra le azioni se necessario