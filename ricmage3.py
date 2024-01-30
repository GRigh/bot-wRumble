import cv2
import numpy as np
import time
from collections import deque
import os
import pyautogui
import random
def deployUnit():
    numero_casuale = random.choice([1, 2, 3, 4])
    if numero_casuale == 1:
        clickOn(1235, 1320, 1190, 1305)
        print("scelta truppa numero 1")
    if numero_casuale == 2:
        clickOn(1379, 1468, 1190, 1305)
        print("scelta truppa numero 2")
    if numero_casuale == 3:
        clickOn(1538, 1604, 1190, 1305)
        print("scelta truppa numero 3")
    if numero_casuale == 4:
        clickOn(1686, 1761, 1190, 1305)
        print("scelta truppa numero 4")
    clickOn(1192, 1691, 723, 947)
    print("deployata unit")
    ritardo_casuale = random.uniform(1, 3)
    time.sleep(ritardo_casuale)
    
def continuu():    
    print("attendo di cliccare su mappa del mondo")
    ritardo_casuale = random.uniform(14, 20)
    time.sleep(ritardo_casuale)
    clickOn(1459, 1486, 1305, 1338);
    print("ho cliccato su mappa del mondo")
    print("attendo di poter tornare agli incarichi su mappa del mondo")
    ritardo_casuale = random.uniform(12, 16)
    time.sleep(ritardo_casuale)
    clickOn(1084, 1217, 1235, 1289);   
    print("tornato agli incarichi... restart ...")    
    print("[...]")

def playGame():
    print("Partita iniziata!!!")
    #clicca sul bottone inizia 
    clickOn(1364, 1464, 1086, 1178)
    gameEnd = False
    while gameEnd == False:
        #fai cose
        # Cattura uno screenshot dinamico con PyAutoGUI
        screenshot = pyautogui.screenshot("gameEnd.png")
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
        immagine_riferimento = cv2.imread('fineGame2.png')

        # Confronta le immagini
        presente = confronta_immagini(immagine_riferimento, screenshot, 190)
        if presente:
            print("game finito")
            gameEnd = True;
        else:
            print("... game ancora in corso ...")
            print("... sto per provare ad eseguire una mossa ...")
            ritardo_casuale = random.uniform(1, 3)
            time.sleep(ritardo_casuale)
            deployUnit()
        
    
def isGameReady():
    # Cattura uno screenshot dinamico con PyAutoGUI
    screenshot = pyautogui.screenshot("ready.png")
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
    immagine_riferimento = cv2.imread('pronto.png')

    # Confronta le immagini
    presente = confronta_immagini(immagine_riferimento, region=(0, 0, 1920, 1080), confidence=0.8)
    if presente:
        print("immagine pronto presente")
        return True
    else:
        print("... caricamento partita ...")
        return False
    
#clicca casualmente in un rettangolo/quadrato definito dalle coordinate
def clickOn(x_min, x_max, y_min, y_max):
    # Genera coordinate casuali all'interno dell'intervallo
    x_coordinate = random.randint(x_min, x_max)
    y_coordinate = random.randint(y_min, y_max)
    # Sposta il mouse nella posizione casuale
    pyautogui.click(x_coordinate, y_coordinate)
    # Genera un ritardo casuale tra 1 e 3 secondi
    ritardo_casuale = random.uniform(1, 3)
    time.sleep(ritardo_casuale)
#muove casualmente in un rettangolo/quadrato definito dalle coordinate 
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
def select_incarico():
    #clicca sul bottone degli incarichi
    clickOn(1100, 1363, 1133, 1188)
    #clicca sul primo incarico
    
    numero_casuale = random.choice([1, 2, 3])
    
    if numero_casuale == 1:
        clickOn(1096, 1234, 1073, 1115)
        print("scelto incarico 1")
    if numero_casuale == 2:
        clickOn(1353, 1487, 1081, 1115)
        print("scelto incarico 1")
    if numero_casuale == 3:
        clickOn(1610, 1737, 1081, 1115)
        print("scelto incarico 1")
    
def confronta_immagini(immagine_riferimento, screenshot, soglia_match):
    def confronta_immagini(image_path, region, confidence=0.8):
    """
    Compare the image located at 'image_path' with the screen region specified by 'region'
    using pyautogui's locateOnScreen function.

    Parameters:
    - image_path: Path to the reference image.
    - region: Tuple (x, y, width, height) specifying the region to search for the image.
    - confidence: Minimum confidence level for the match (default is 0.8).

    Returns:
    - True if the image is found with the specified confidence level, False otherwise.
    """
    # Wait for a short time to ensure the screen is updated
    time.sleep(1)

    # Use pyautogui's locateOnScreen function to find the image
    match = pyautogui.locateOnScreen(image_path, region=region, confidence=confidence)

    # If a match is found, return True, else return False
    return match is not None

while True:
    # Cattura uno screenshot dinamico con PyAutoGUI
    gameCanStart = False
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    

    # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
    immagine_riferimento = cv2.imread('incarico.png')

    # Confronta le immagini
    presente = confronta_immagini('incarico.png', region=(0, 0, 1920, 1080), confidence=0.8)

    if presente:
        print("L'immagine è presente nello screenshot.")
        select_incarico()
        while gameCanStart == False:
           gameCanStart = isGameReady()
           # gameCanStart = False
           time.sleep(1)
        playGame()
        continuu()
    else:
        print("L'immagine non è presente nello screenshot.")

    # Salva il nuovo screenshot nella coda e cancella quelli più vecchi
    coda_screenshot = deque(maxlen=5)  # Imposta la lunghezza massima della coda a 5 (o qualsiasi valore desiderato)
    coda_screenshot.append(screenshot)

    # Cancellare gli screenshot più vecchi
    for idx, img in enumerate(coda_screenshot):
        cv2.imwrite(f'old_screenshot_{idx}.png', img)
    
    # Aggiungi un ritardo tra le iterazioni del loop (ad esempio, 1 secondo)
    time.sleep(1)