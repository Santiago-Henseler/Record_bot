# Meet_record_bot
Boot para grabar reuniones de google meet

# Setup

Para poder utilizar esta aplicaciòn hay que tener instalado [Python3](https://www.python.org/downloads/) e instalar la siguiente libreria:

```bash
pip install pyautogui
```

Ademas hay que instalar [ffmpeg](https://ffmpeg.org/)  para la captura de audio y video

```bash
sudo apt install ffmpeg
```

Para encntrar el usuario para unirse a la reunion de meet lo buscas en la siguiente carpeta:

```bash
cd /$HOME/.config/google-chrome
```

Aparecen varias carpetas y  las que digan ``` Profile x``` ,siendo la x el numero de perfil a seleccionar, va a ser la que deben agregar en el script 


