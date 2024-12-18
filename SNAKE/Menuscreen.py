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


FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.blit(menu_screen_draw(), (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
