import os
import sys
import random
import subprocess
import speech_recognition as sr
from datetime import datetime
import pygame

# Inicializar el reconocimiento de voz
recognizer = sr.Recognizer()

# Inicializar el motor de audio
pygame.mixer.init()

# Obtener la ruta correcta de los recursos empaquetados
def get_resource_path(relative_path):
    try:
        # Si el script se está ejecutando desde el ejecutable empaquetado
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        # Si el script se está ejecutando normalmente
        return os.path.join(os.path.abspath("."), relative_path)
    except Exception as e:
        print(e)
        return None

# Función para reproducir el archivo de audio
def play_audio(file_name):
    # Obtener la ruta completa del archivo de audio
    file_path = get_resource_path(f"voces/{file_name}.mp3")
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    else:
        print(f"Archivo {file_name}.mp3 no encontrado")

# Inicializar el reconocedor de voz
def listen():
    # Usar el micrófono como fuente de entrada
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        return audio


# Reconocer el comando
def recognize_command(audio):
    try:
        # Reconocer el texto de lo que se dijo
        command = recognizer.recognize_google(audio, language="es-ES").lower()
        print("Comando recibido:", command)
        return command
    except sr.UnknownValueError:
        play_audio("Repetir")
        return None
    except sr.RequestError:
        play_audio("Problemas")
        return None

# Ejecutar el comando
def execute_command(command):
    if "mercy" in command:  # Solo responder si la palabra "mercy" está presente
        if "apaga el ordenador" in command:
            play_audio("Apagando el ordenador")
            os.system("shutdown /s /f /t 0")  # En Windows
        elif "reinicia el ordenador" in command:
            play_audio("Reiniciando el ordenador")
            os.system("shutdown /r /f /t 0")  # En Windows
        elif "cierra opera" in command:
            play_audio("Cerrando el navegador")
            os.system("taskkill /f /im opera.exe")  # Cerrar Opera GX
        elif "abre opera" in command:
            play_audio("Abriendo el navegador")
            os.system("start opera")  # Abrir Opera GX
        elif "abre steam" in command:
            play_audio("Abriendo Steam")
            os.system("start steam")  # En Windows
        elif "abre la calculadora" in command:
            play_audio("Abriendo la calculadora")
            os.system("calc")  # En Windows
        elif "cierra spotify" in command:
            play_audio("Cerrando Spotify")
            os.system("taskkill /f /im spotify.exe")  # En Windows
        elif "bloquea el ordenador" in command:
            play_audio("Bloqueando el ordenador")
            os.system("rundll32.exe user32.dll,LockWorkStation")  # En Windows
        elif "minimiza todas las ventanas" in command:
            play_audio("Minimizando todas las ventanas")
            os.system("nircmdc.exe win min all")  # Si tienes nircmdc.exe
        elif "abre discord" in command:
            play_audio("Abriendo Discord")
            os.system("start discord")  # En Windows
        elif "cierra discord" in command:
            play_audio("Cerrando Discord")
            os.system("taskkill /f /im discord.exe")  # En Windows
        elif "pon discord en no molestar" in command:
            play_audio("Poniendo Discord en no molestar")
            subprocess.call('discord --status "dnd"')  # Si Discord está en el PATH
        elif "pon discord en online" in command:
            play_audio("Poniendo Discord en estado online")
            subprocess.call('discord --status "online"')  # Si Discord está en el PATH
        elif "pon discord en invisible" in command:
            play_audio("Poniendo Discord en estado invisible")
            subprocess.call('discord --status "invisible"')  # Si Discord está en el PATH
        elif "pon discord en afk" in command:
            play_audio("Poniendo Discord en estado AFK")
            subprocess.call('discord --status "afk"')  # Si Discord está en el PATH
        elif "pausa la musica" in command:
            play_audio("Pausando la musica")
            os.system("nircmdc.exe sendkeypress playpause")  # Pausar música
        elif "reanuda la musica" in command:
            play_audio("Reanudando la musica")
            os.system("nircmdc.exe sendkeypress playpause")  # Reanudar música
        elif "siguiente cancion" in command:
            play_audio("Pasando a la siguiente cancion")
            os.system("nircmdc.exe sendkeypress media_next")  # Cambiar a la siguiente canción
        elif "salir" in command:
            play_audio("Saliendo")
            sys.exit()
        else:
            play_audio("Comando no reconocido")

# Función principal
def main():
    play_audio("Saludo")  # Saludo inicial
    while True:
        audio = listen()  # Escuchar lo que dices
        command = recognize_command(audio)  # Reconocer el comando
        
        if command and "mercy" in command:  # Solo activar si se dice "Mercy"
            execute_command(command)  # Ejecutar el comando

if __name__ == "__main__":
    main()
