import cv2
import numpy as np
import time
from collections import deque
import os
import pyautogui
import random
import logging

# Configure the logging module
logging.basicConfig(filename='output_log.txt', level=logging.INFO)
###
#TODO assolutamente riscrivere il codice, troppi pezzi ripetuti
#TODO 18-11-2023 clkick più "umani" -> rifare i click durante il deploy e il metodo di deploy unit va reso più umano -> click vanno fatti diventare trascinazioni, sempre random da Pcoordinata1 a Pcoordinata2,
#TODO            sempre tutto in tempistiche random // aggiungere scroll (trascinata) sia basso che alto in partita, probabilemente ogni 2/3 deployate, maximizzare la randomicità dove possibile
#TODO 20/25-11-2023 implementare funzione per battere crash blizzard, migliorare deploy unit più efficace

def checkTimeFrame(timeFrameIniziale, timeFrameFinale, differenzaSecondi):
    differenza_tempo = timeFrameFinale - timeFrameIniziale
    return differenza_tempo >= differenzaSecondi
    # Esempio di utilizzo
    # timeFrameIniziale = time.time()  # Timestamp iniziale
    # time.sleep(10)  # Simuliamo un passare di tempo di 10 secondi
    # timeFrameFinale = time.time()  # Timestamp finale

def levelUp():
    print("start check level UP")
    ritardo_casuale = random.uniform(4, 5.5)
    time.sleep(ritardo_casuale) 
    A = [(1105, 413), (1109, 400), (1115, 375), (1126, 375), (1130, 400), (1138, 415), (1121, 404)]
    L = [(1508, 376), (1509, 411), (1528, 412)]
    esclamativo = [(1735, 375), (1735, 385), (1735, 412)]

    negativoA = [(1120, 414), (1098, 387), (1141, 388)]
    negativoL = [(1521, 396), (1493, 397)]

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
        logging.info("[...]LVL UP!")
        clickOn(1608, 1766, 546, 640)
    else: 
        print("Lettere NON trovate")
    
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
    
def isCompleted():
    # Cattura uno screenshot dinamico con PyAutoGUI
    screenshot = pyautogui.screenshot(region=(1059, 1070, 729, 213)).save("checkCompleted.png")
    imgScreenshot = cv2.imread("checkCompleted.png")
    screenshot = cv2.cvtColor(np.array(imgScreenshot), cv2.COLOR_RGB2BGR)
    # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
    immagine_riferimento = cv2.imread('completed.png')

    # Confronta le immagini
    presente = confronta_immagini(immagine_riferimento, screenshot, 80)
    if presente:
        print("(1) Trovato reward incarico, provo a riscattarlo")
        logging.info("(1) Trovato reward incarico, provo a riscattarlo")
        clickOn(1353, 1487, 1081, 1115)
        ritardo_casuale = random.uniform(3.2, 4.3)
        time.sleep(ritardo_casuale)
        levelUp()
    else: 
        print("(1) reward NON trovato, provo a selezionare incarico un altra volta")

def deployUnit():
    i = 0
    numero_casuale_deploy = random.choice([1, 2, 3])
    while i < numero_casuale_deploy:
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
        ritardo_casuale = random.uniform(0.1, 0.4)
        time.sleep(ritardo_casuale)
        i = i + 1
    
def continuu():    
    print("Game finito, check se vittoria o sconfitta")
    logging.info("Game finito, check se vittoria o sconfitta")
    ritardo_casuale = random.uniform(7.4, 10.5)
    time.sleep(ritardo_casuale)
    #prima cosa vedere se è sconfitta o vittoria 
    pixel_color = pyautogui.pixel(1574, 206)
    # Check if the first and third elements are 255 and 0, respectively
    time.sleep(5)
    if pixel_color[0] == 255 and pixel_color[2] == 0:
        print("Vittoria")
        vittoria = True
    else:
        print("Sconfitta")
        vittoria = False
    clickOn(1501, 1651, 1314, 1343)
    

def playGame():
    print("!!! Partita iniziata !!!")
    logging.info("!!! Partita iniziata !!!")
    #clicca sul bottone inizia 
    ritardo_casuale = random.uniform(3, 4)
    time.sleep(ritardo_casuale)
    clickOn(1364, 1464, 1086, 1178)
    gameEnd = False
    ritardo_casuale = random.uniform(1, 2.6)
    time.sleep(ritardo_casuale)
    while gameEnd == False:      #TODO IN CORSO da rifare il check di fine partita e timing deploy units, probabilmente va rivisto anche il deploy delle units in se
        time.sleep(1)
        # Get the RGB values of the pixel at the specified coordinates
        pixel_color = pyautogui.pixel(1472, 99)
        # Check if the pixel color is white (255, 255, 255)
        if pixel_color == (255, 255, 255):
            print("SEG: Timer visibile")
            logging.info("SEG: Timer visibile")
            #waitForDeploying()
            deployUnit()
            ritardo_casuale = random.uniform(8.2, 10.3) #attenzione! fare check più frequenti per vedere end game
            time.sleep(ritardo_casuale)
        else: 
            print("SEG: Timer NON visibile")
            logging.info("SEG: Timer NON visibile")
            gameEnd = True
            ritardo_casuale = random.uniform(4, 5)
            time.sleep(ritardo_casuale)
        
    
def isGameReady():
    # Cattura uno screenshot dinamico con PyAutoGUI
    screenshot = pyautogui.screenshot(region=(1343, 1057, 160, 210)).save("ready.png")
    imgScreenshot = cv2.imread("ready.png")
    screenshot = cv2.cvtColor(np.array(imgScreenshot), cv2.COLOR_RGB2BGR)
    # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
    immagine_riferimento = cv2.imread('pronto.png')

    # Confronta le immagini
    presente = confronta_immagini(immagine_riferimento, screenshot, 88)
    if presente:
        print("Immagine pronto presente")
        logging.info("Immagine pronto presente")
        return True
    else:
        print("... Caricamento partita ...")
        logging.info("... Caricamento partita ...")
        
        return False
    
#clicca casualmente in un rettangolo/quadrato definito dalle coordinate
def clickOn(x_min, x_max, y_min, y_max):
    # Genera coordinate casuali all'interno dell'intervallo
    x_coordinate = random.randint(x_min, x_max)
    y_coordinate = random.randint(y_min, y_max)
    # Sposta il mouse nella posizione casuale
    pyautogui.click(x_coordinate, y_coordinate)
    # Genera un ritardo casuale tra 1 e 3 secondi
    ritardo_casuale = random.uniform(0.2, 0.34)
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
    preIncarico = True
    while preIncarico:
        #clicca sul bottone degli incarichi
        print("(1) Inizio selezione incarico")
        logging.info("(1) Inizio selezione incarico")
        ritardo_casuale = random.uniform(1, 2)
        time.sleep(ritardo_casuale)
        clickOn(1100, 1363, 1133, 1188)
        ritardo_casuale = random.uniform(1, 2)
        time.sleep(ritardo_casuale)
        print("Provo a selezionare incarico")
        logging.info("Provo a selezionare incarico")
        # Cattura uno screenshot dinamico con PyAutoGUI
        screenshot = pyautogui.screenshot(region=(1073, 1051, 697, 81)).save("3incarichi.png")
        imgScreenshot = cv2.imread("3incarichi.png")
        screenshot = cv2.cvtColor(np.array(imgScreenshot), cv2.COLOR_RGB2BGR)
        # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
        immagine_riferimento = cv2.imread('3incarichiCheck.png')

        # Confronta le immagini
        presente = confronta_immagini(immagine_riferimento, screenshot, 90)
        if presente:
            numero_casuale = random.choice([1, 2, 3])
            if numero_casuale == 1:
                clickOn(1096, 1234, 1073, 1115)
                print("scelto incarico 1")
                logging.info("scelto incarico 1")
            if numero_casuale == 2:
                clickOn(1353, 1487, 1081, 1115)
                print("scelto incarico 2")
                logging.info("scelto incarico 2")
            if numero_casuale == 3:
                clickOn(1610, 1737, 1081, 1115)
                print("scelto incarico 3")
                logging.info("scelto incarico 3")
            preIncarico = False
        else:
            print("(1) Selezione incarico non possibile, controllo se presente REWARD")
            logging.info("(1) Selezione incarico non possibile, controllo se presente REWARD")
            isCompleted()
        time.sleep(1)
        
def confronta_immagini(immagine_riferimento, screenshot, soglia_match):
    # Converti le immagini in scala di grigi
    # Normalizza le immagini
    gray_riferimento = cv2.cvtColor(immagine_riferimento, cv2.COLOR_BGR2GRAY)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # Esegui il matching dei descrittori ORB
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(gray_riferimento, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray_screenshot, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    if descriptors1 is None:
        print("Errore descrittore 1")
        logging.info("Errore descrittore 1")
        return False
    if descriptors2 is None:
        print("Errore descrittore 2")
        logging.info("Errore descrittore 2")
        return False
    matches = bf.match(descriptors1, descriptors2)
    
    # Ordina i match in base alla distanza
    matches = sorted(matches, key=lambda x: x.distance)
    print(f"[...]Lunghezza match: {len(matches)}")
    logging.info(f"[...]Lunghezza match: {len(matches)}")
    # Se ci sono abbastanza match, l'immagine è presente
    if len(matches) > soglia_match:
        return True
    else:
        return False


VS = 0
cont_try_select = 0;
while True:
    # Cattura uno screenshot dinamico con PyAutoGUI
    ritardo_casuale = random.uniform(3.7, 6.5)
    time.sleep(ritardo_casuale)
    gameCanStart = False
    screenshot = pyautogui.screenshot(region=(1064, 1110, 730, 280))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    

    # Carica l'immagine di riferimento (l'immagine che vuoi cercare)
    immagine_riferimento = cv2.imread('incarico.png')

    # Confronta le immagini
    presente = confronta_immagini(immagine_riferimento, screenshot, 310)

    if presente:
        cont_try_select = 0
        select_incarico()
        ritardo_casuale = random.uniform(22, 25)
        time.sleep(ritardo_casuale)
        while gameCanStart == False:
           gameCanStart = isGameReady()
           print("precaricamento partita")
           logging.info("precaricamento partita")
           time.sleep(1)
           # gameCanStart = False
        playGame() #esce da solo se crasha/shadoban
        levelUp()
        continuu()
        VS = VS + 1
    else:
        print("L'immagine non è presente nello screenshot.")
        logging.info("Schermata incarichi non trovata")
        cont_try_select = cont_try_select + 1
        if cont_try_select % 5 == 0:
            clickOn(1284, 1494, 1277, 1355)
            print("clicco sulla mappa")
    print(VS)
    # Salva il nuovo screenshot nella coda e cancella quelli più vecchi
    coda_screenshot = deque(maxlen=5)  # Imposta la lunghezza massima della coda a 5
    coda_screenshot.append(screenshot)

    # Cancellare gli screenshot più vecchi
    for idx, img in enumerate(coda_screenshot):
        cv2.imwrite(f'old_screenshot_{idx}.png', img)
   
    time.sleep(1)