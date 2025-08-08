import os
import sys
import pyautogui
import time
from datetime import date
from datetime import datetime

REUNION = "" # Link a la reunion de la reunion
GOOGLEPROFILE = "$HOME/santy/.config/google-chrome/Profile 2"  # El perfil con el que queres entrar a la reunion (solo si es google meet)
DURACION = "3:10:00"
INICIO = 18

def meet():
    os.system("google-chrome "+ REUNION +" --new-window --user-data-dir="+ GOOGLEPROFILE +"&")

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

if __name__ == "__main__":
    inicio = True

    while inicio:
        ahora = datetime.now()
        if ahora.hour == INICIO:
            inicio = False
            
            if REUNION.__contains__("meet") :
                meet()
            else:
                print("aca")


        time.sleep(30)
