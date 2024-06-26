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

def is_colision(snake_head, apple):
    if snake_head[0] == apple[0] and snake_head[1] == apple[1]:
        return True
    return False

def is_self_collision(snake):
    head = snake[0]
    for part in snake[1:]:
        if head == part:
            return True
    return False

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() # Objekt
    window = pygame.display.set_mode(config.ROZLISENIE)
    # Suradnica hlavy hadika - teraz urobim telo hada, obalim ho do pola
    had = [[config.ROZLISENIE[0]//2, config.ROZLISENIE[1]//2]]
    smer = "DOWN" # Definujeme defaultný smer
    jablko = generate_apple(config.ROZLISENIE, config.VELKOST_JABLKA)
    pocitadlo_zjedenych_jablk = 0  # Zavednie počítadla pre zjedené jablka

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu
        
        keys = pygame.key.get_pressed() # Vrati slovnik, kde je klávesy , či sú stlačné alebo nie, (True, False)
        smer = update_direction(smer, keys)
        # Tu nastane zmena, lebo už bude telo hada, teda nebude had ale new_position
        # had = update_position(had, smer, config.VELKOST_HADA) # Mení sa pohyb hlavičky hada v závislosti, ako je nastavený defaultný smer

        new_position = update_position(had[0], smer, config.VELKOST_HADA)
        had.insert(0, new_position)

        if is_colision(had[0], jablko):
            pocitadlo_zjedenych_jablk += 1
            print('NASTALA KOLIZIA')
            jablko = generate_apple(config.ROZLISENIE, config.VELKOST_HADA)
        else:
            had.pop()

        # Kontrola či hlava hadika je von, dáme index 0, lebo hlava je na nulke pozicii v poli
        if is_out(had[0], config.ROZLISENIE) or is_self_collision(had):
            end_game(window)

        # Vykreslenie hlavičky hadika
        # pygame.draw.rect(window, config.FARBA_HLAVY_HADA, pygame.Rect(had[0], had[1], config.VELKOST_HADA, config.VELKOST_HADA))

        # To bude inak, lebo to už bude had s telom, teda list listov a navyše chceme inú farbu pre hlavu a telo hada
        #for part in had:
           #pygame.draw.rect(window, config.FARBA_HLAVY_HADA, pygame.Rect(part[0], part[1], config.VELKOST_HADA, config.VELKOST_HADA))

        for i, part in enumerate(had):
            if i == 0:
                pygame.draw.rect(window, config.FARBA_HLAVY_HADA, pygame.Rect(part[0], part[1], config.VELKOST_HADA, config.VELKOST_HADA))
            else:
                 pygame.draw.rect(window, config.FARBA_TELO_HADA, pygame.Rect(part[0], part[1], config.VELKOST_HADA, config.VELKOST_HADA))

        # Vykreslenie jablka
        pygame.draw.rect(window, config.FARBA_JABLKA, pygame.Rect(jablko[0], jablko[1], config.VELKOST_JABLKA, config.VELKOST_JABLKA))

         # Vypis pocitadla
        font = pygame.font.Font(None, 36)
        pocitadlo_text = font.render("Počet zjedených jabĺk: " + str(pocitadlo_zjedenych_jablk), True, (255, 255, 255))
        window.blit(pocitadlo_text, (10, 10))

        pygame.display.update()

        # Spomalenie cyklu
        window.fill(config.FARBA_POZADIA) # Premazanie obrazovky
        clock.tick(config.FPS) # Obnova hada - resp.obrázkov