import pygame
from Config import config
import sys

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() # Objekt
    window = pygame.display.set_mode(config.ROZLISENIE)
    # Suradnica hlavy hadika 
    had = [config.ROZLISENIE[0]//2, config.ROZLISENIE[1]//2]

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu

        # Vykreslenie hlavičky hadika
        pygame.draw.rect(window, config.FARBA_HLAVY_HADA, pygame.Rect(had[0], had[1], config.VELKOST_HADA, config.VELKOST_HADA))

        
        pygame.display.update()

        # Spomalenie cyklu
        window.fill(config.FARBA_POZADIA) # Premazanie obrazovky
        clock.tick(config.FPS) # Obnova hada - resp.obrázkov