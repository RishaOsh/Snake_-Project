import pygame
from pygame.draw import *
pygame.init()

TEXTHEAD = pygame.font.SysFont(pygame.font.get_default_font(), 30)
TEXTMAIN = pygame.font.SysFont(pygame.font.get_default_font(), 25)

def menu_screen_draw():
    menu = pygame.Surface((400,400))
    snake_head = TEXTHEAD.render("SNAKE GAME", True, (225, 225, 225))
    menu.blit(snake_head, (140, 90))

    rect(menu, (255, 255, 255), (140, 165, 153, 27), 2)
    press_to_start = TEXTMAIN.render("PRESS TO START", True, (225, 225, 225))
    menu.blit(press_to_start, (145, 170))
    return menu

def menu_quit():
    GAME_STAGE = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STAGE = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            xm = event.pos[0]
            ym = event.pos[1]
            GAME_STAGE = 2

        return GAME_STAGE
