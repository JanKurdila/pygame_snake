import pygame
from Config import config
import sys
import random

def update_position(snake, direction, step):
    if direction == "UP":
        snake = [snake[0],snake[1]-step]
    if direction == "DOWN":
        snake = [snake[0],snake[1]+step]
    if direction == "RIGHT":
        snake = [snake[0]+step,snake[1]]
    if direction == "LEFT":
        snake = [snake[0]-step,snake[1]]
    return snake

def update_direction(direction, keys):
    if keys[pygame.K_LEFT]:
        return 'LEFT' if direction != 'RIGHT' else direction
    if keys[pygame.K_RIGHT]:
        return 'RIGHT' if direction != 'LEFT' else direction
    if keys[pygame.K_UP]:
        return 'UP' if direction != 'DOWN' else direction
    if keys[pygame.K_DOWN]:
        return 'DOWN' if direction != 'UP' else direction
    return direction

def is_out(snake, game_res):
    if snake[0] < 0 or snake[1] < 0 or  snake[0] > game_res[0] or snake[1] > game_res[1]:
        return True
    return False

def end_game(window):
    print('GAME OVER')
    window.fill(config.FARBA_POZADIA)
    pygame.quit()
    sys.exit()

def generate_apple(game_res, snake_size):
    x = random.choice(range(0, game_res[0]-snake_size + 1, snake_size))
    y = random.choice(range(0, game_res[1]-snake_size + 1, snake_size))
    return [x, y]

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() # Objekt
    window = pygame.display.set_mode(config.ROZLISENIE)
    # Suradnica hlavy hadika 
    had = [config.ROZLISENIE[0]//2, config.ROZLISENIE[1]//2]
    smer = "DOWN" # Definujeme defaultný smer
    jablko = generate_apple(config.ROZLISENIE, config.VELKOST_HADA)

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu
        
        keys = pygame.key.get_pressed() # Vrati slovnik, kde je klávesy , či sú stlačné alebo nie, (True, False)
        smer = update_direction(smer, keys)
        had = update_position(had, smer, config.VELKOST_HADA) # Mení sa pohyb hlavičky hada v závislosti, ako je nastavený defaultný smer

        # Kontrola či hlava hadika je von
        if is_out(had, config.ROZLISENIE):
            end_game(window)

        # Vykreslenie hlavičky hadika
        pygame.draw.rect(window, config.FARBA_HLAVY_HADA, pygame.Rect(had[0], had[1], config.VELKOST_HADA, config.VELKOST_HADA))

        # Vykreslenie jablka
        pygame.draw.rect(window, config.FARBA_JABLKA, pygame.Rect(jablko[0], jablko[1], config.VELKOST_HADA, config.VELKOST_HADA))

        pygame.display.update()

        # Spomalenie cyklu
        window.fill(config.FARBA_POZADIA) # Premazanie obrazovky
        clock.tick(config.FPS) # Obnova hada - resp.obrázkov