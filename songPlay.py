import os
from re import X
from tkinter import Y
import pygame

song = "/Users/chathurawijekoon/Desktop/Python/Test App/Songs/test.mp3"
pygame.init()
pygame.mixer.music.load(song)

while True:
    pygame.mixer.music.play()