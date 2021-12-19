import pygame
import pygame.pkgdata
import src.test
from pygame.locals import *

def main():

    WIDTH = 1280
    HEIGHT = 720

    tester = src.test

    text = tester.test()
    # Initialise screen
    pygame.init()
    flags = pygame.SCALED | pygame.RESIZABLE
    screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, vsync=1)
    pygame.display.set_caption("Noxphor")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Display some text
    font_data = pygame.pkgdata.getResource("freesansbold.ttf")
    font = pygame.font.Font(font_data, 36)
    text = font.render(text, 1, (250, 250, 250))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('cya')
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == "__main__": main()