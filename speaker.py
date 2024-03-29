from termcolor import colored
import pygame
import os
import settings

def speak(text,lang=settings.lang):
    print(colored(f"{settings.botname}: {text}",settings.bot_console_color))

    os.system(f"espeak -v {lang} '{text}'")

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()