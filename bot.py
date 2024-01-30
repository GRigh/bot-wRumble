import pyautogui
import time

# Attendiamo alcuni secondi prima di iniziare, in modo che tu possa passare alla finestra giusta
time.sleep(5)

# Coordinate iniziali del trascinamento
start_x = 100
start_y = 100

# Coordinate finali del trascinamento
end_x = 1000
end_y = 1000

# Eseguiamo il trascinamento del mouse dalle coordinate iniziali a quelle finali
pyautogui.moveTo(start_x, start_y)
pyautogui.dragTo(end_x, end_y, duration=1)  # La durata specifica la velocità del trascinamento