import cv2
import numpy as np
import time
from collections import deque
import os

def confronta_immagini(immagine_riferimento, screenshot):
    # Converti le immagini in scala di grigi
    gray_riferimento = cv2.cvtColor(immagine_riferimento, cv2.COLOR_BGR2GRAY)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Esegui il matching dei descrittori ORB
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(gray_riferimento, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray_screenshot, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    # Ordina i match in base alla distanza
    matches = sorted(matches, key=lambda x: x.distance)

    # Se ci sono abbastanza match, l'immagine è presente
    soglia_match = 20
    if len(matches) > soglia_match:
        return True
    else:
        return False

while True:
    # Cattura lo screenshot
    screenshot = cv2.imread('screenshot.png')

    # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
    immagine_riferimento = cv2.imread('incarico.png')
    

    # Confronta le immagini
    presente = confronta_immagini(immagine_riferimento, screenshot)

    if presente:
        print("L'immagine è presente nello screenshot.")
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