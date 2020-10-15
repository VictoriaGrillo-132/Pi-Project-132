import os
from tkinter import *
from datetime import datetime
import pygame



#current version of the game
TITLE = "Event Horizon"
VERSION = 0.0
LAST_UPDATE = datetime.fromtimestamp(os.path.getmtime(__file__))
AUTHOR = 'JA, ID, VG'


#setting GUI size
width = 900
height = 500
#window= Tk()
#window.geometry('{}x{}'.format(width, height))
#window.title(TITLE)
#screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#setting up the keys for the game
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#initialize pygame
pygame.init()

#to keep the game running
running = True

#Main loop for game
while running:
    for event in pygame.event.get():
        #seeing if the player or user hits a key
        if event.type == KEYDOWN:
            #if escape key is pressed, it will stop the loop
            if event.key == K_ESCAPE:
                running = False
        #if the player chooses to close the game
        elif event.type == QUIT:
            running = False

#setting the screen white
screen.fill((255,255,255))

#Creating the surface and pass in the tuple containing width and length
surf = pygame.Surface((50, 50))
#giving the surface a color so it can be separate from the background
surf.fill((0, 0, 0))
rect = surf.get.rect()






