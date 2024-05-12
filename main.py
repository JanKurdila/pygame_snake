import pygame
from Config import config
import sys

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode(config.ROZLISENIE)

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu

        pygame.display.update()