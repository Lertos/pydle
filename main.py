import pygame
import pygame.pkgdata

import src.key_handler as keys
import src.panel as panel

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
pygame.display.set_caption('Noxphor')

TEXT_DATA = pygame.pkgdata.getResource('freesansbold.ttf')
TEXT_FONT = pygame.font.Font(TEXT_DATA, 20)

keyHandler = keys.KeyHandler(pygame)

characterPanel = panel.Panel(pygame, WINDOW, TEXT_FONT, False, 360, 700, (50, 80, 120), 10, 10, 10, 10)
#Temporary until we can pass things to this method
text = [
    'white::Name Lertos::',
    'yellow::Gold::white::100$::',
    'red::Health::white::200::'
]
characterPanel.setTextToDraw(text)

mainPanel = panel.Panel(pygame, WINDOW, TEXT_FONT, False, 890, 500, (150, 80, 50), 380, 10, 10, 10)
#Temporary until we can pass things to this method
text = [
    'yellow::1::white::TravelTravelTravel::',
    '\n::',
    'yellow::2::white::Make Campfire::',
    'yellow::3::white::Eat::'
]
mainPanel.setTextToDraw(text)


chatPanel = panel.Panel(pygame, WINDOW, TEXT_FONT, False, 890, 190, (30, 150, 50), 380, 520, 10, 10)
#Temporary until we can pass things to this method
text = [
    'white::Chat Panel',
    '',
    'white::You did 0 damage to the Rat'
]
chatPanel.setTextToDraw(text)


def draw(panels):
    WINDOW.fill(BLACK)
    
    text = TEXT_FONT.render(keyHandler.getAllKeys(), 1, WHITE)
    textPosition = text.get_rect()
    textPosition.centerx = WINDOW.get_rect().centerx
    textPosition.centery = WINDOW.get_rect().centery
    WINDOW.blit(text, textPosition)

    for panel in panels:
        panel.drawPanel()

    pygame.display.update()
    

def main():
    #Ensures that the frames per second are enforced
    fpsClock = pygame.time.Clock()
    
    panels = []
    panels.append(characterPanel)
    panels.append(mainPanel)
    panels.append(chatPanel)
    
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

        draw(panels)
        
        if keyHandler.clearKeysNextFrame:
            keyHandler.clearKeys()
            keyHandler.clearKeysNextFrame = False


if __name__ == '__main__': main()