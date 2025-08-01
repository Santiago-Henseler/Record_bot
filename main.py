import os
import sys
import pyautogui
import time
from datetime import date
from datetime import datetime

MEET = "" # Link al google meet de la reunion
GOOGLEPROFILE = "$HOME/santy/.config/google-chrome/Profile 2"  # El perfil con el que queres entrar a la reunion
DURACION = "3:10:00"
INICIO = 19

inicio = True

while inicio:
    ahora = datetime.now()
    if ahora.hour == INICIO:
        inicio = False
        os.system("google-chrome "+ MEET +" --new-window --user-data-dir="+ GOOGLEPROFILE +"&")

        time.sleep(5)

        try:
            button = pyautogui.locateOnScreen("img/boton.png")
            center = pyautogui.center(button)
            pyautogui.click(center)
        except:
            try:
                button = pyautogui.locateOnScreen("img/boton2.png")
                center = pyautogui.center(button)
                pyautogui.click(center)
            except: 
                print("Error al encontrar el boton para unirse a la reunion")
                sys.exit(-1)

        os.system("ffmpeg -video_size 1920x1080 -framerate 30 -f x11grab -i :0.0 -f pulse -i default -t "+DURACION+" clase-"+date.today().strftime('%d-%m-%Y')+".mp4 &")
        sys.exit(0)
    time.sleep(30)