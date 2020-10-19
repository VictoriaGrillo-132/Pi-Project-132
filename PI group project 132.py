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

    #getting the key that is currently being pressed
    pressed_keys = pygame.key.get_pressed()
    #updating player sprite due to the user pressing the keys
    player.update(pressed_keys)

    #screen filled with black
    screen.fill((0, 0, 0))
    

#setting the screen white
screen.fill((255,255,255))

#Creating the surface and pass in the tuple containing width and length
surf = pygame.Surface((50, 50))
#giving the surface a color so it can be separate from the background
surf.fill((0, 0, 0))
rect = surf.get.rect()

#making the player object by using pygmae.sprite.Sprite
#This allows us to make the game how we want i.e. making the player start on one side of the
#screena and also have the attacks come from the other side of the screen
class Player(pygame.sprite.Sprite):
    super(Player, self).__init__()
    self.surf = pygame.Surface((75, 25))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect()

#filling the screen black
screen.fill((0,0,0))

#Having the player drawn on the screen
screen.blit(player.surf, player.rect)
#updating the display for the game
pygame.display.flip()


#setting up the keys for the user to use for the game
pressed_keys = pygame.key.get_pressed()
#moving the sprite from the keys that are pressed by the user
def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

    #keeping the player from going out of bounds
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT

    






