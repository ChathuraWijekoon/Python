import os
import pygame

inputdirectory = "/Users/chathurawijekoon/Desktop/Python/Test App/Songs" # Insert the song files folder path here

list = os.listdir("/Users/chathurawijekoon/Desktop/Python/Test App/Songs") # Insert the song files folder path here
print(list)

song = input("\nEnter the song file: ")
file = os.path.join(inputdirectory, song)

pygame.init()
pygame.mixer.music.load(file)

while True:
    n = input("\nType Play or Stop to start or stop the song.\nType Exit to stop the program:\n")
    if n == "play":
        pygame.mixer.music.play()
    elif n == "stop":
        pygame.mixer.music.pause()
    elif n == "exit":
        exit()