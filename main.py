import pygame
import pygame.pkgdata

import src.key_handler as keys

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

keyHandler = keys.KeyHandler(pygame)


def draw():
    WINDOW.fill(BLACK)
    
    text = TEXT_FONT.render(keyHandler.getAllKeys(), 1, WHITE)
    textPosition = text.get_rect()
    textPosition.centerx = WINDOW.get_rect().centerx
    textPosition.centery = WINDOW.get_rect().centery
    WINDOW.blit(text, textPosition)

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
            
            if event.type == pygame.KEYDOWN:
                key = event.key
                
                if key == pygame.K_BACKSPACE:
                    keyHandler.removeCharacter()
                elif key == pygame.K_RETURN:
                    keyHandler.clearKeysNextFrame = True
                elif key == pygame.K_f:
                    keyHandler.startMultiKeyMode()
                elif key == pygame.K_s:
                    keyHandler.startSingleKeyMode()
                else:
                    keyHandler.addPressedKey(key)

        draw()
        
        if keyHandler.clearKeysNextFrame:
            keyHandler.clearKeys()
            keyHandler.clearKeysNextFrame = False


if __name__ == "__main__": main()