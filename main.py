import pygame
import pygame.pkgdata

import src.key_handler

from pygame.locals import *
from time import sleep


WIDTH = 1280
HEIGHT = 720

FPS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Initialise the screen
pygame.init()

FLAGS = pygame.SCALED | pygame.RESIZABLE
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, vsync=1)
pygame.display.set_caption("Noxphor")

TEXT_DATA = pygame.pkgdata.getResource("freesansbold.ttf")
TEXT_FONT = pygame.font.Font(TEXT_DATA, 24)




def draw():
    WINDOW.fill(BLACK)
    text = TEXT_FONT.render("Test Text", 1, WHITE)
    textpos = text.get_rect()
    textpos.centerx = WINDOW.get_rect().centerx
    textpos.centery = WINDOW.get_rect().centery
    WINDOW.blit(text, textpos)

    pygame.display.update()


def main():
    #Ensures that the frames per second are enforced
    fpsClock = pygame.time.Clock()
    
    #Game loop
    while 1:
        fpsClock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        #Get the key presses
        keys_pressed = pygame.key.get_pressed()


        draw()
        


if __name__ == "__main__": main()