import pygame
from pygame.draw import *
from random import randint
from rgbhsl import intRGB
from snakesss import snake_move, snake_draw, snake_long
from Menuscreen import *

global GAME_STAGE
GAME_STAGE = 1

x = [0, 10, 20, 30]
y = [0, 10, 20, 30]
H = [0, 10, 20, 30]

snake = x, y, H

pygame.init()
FPS = 20

screen = pygame.display.set_mode((400, 400))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
# что-то со временем (?)

while not finished:
    clock.tick(FPS)
    if GAME_STAGE == 0:
        finished = True
    if GAME_STAGE == 1:
        screen.blit(menu_screen_draw(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_STAGE = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                xm = event.pos[0]
                ym = event.pos[1]
                GAME_STAGE = 2
    if GAME_STAGE == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_STAGE = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                xm = event.pos[0]
                ym = event.pos[1]
                GAME_STAGE = 1
            if event.type == pygame.MOUSEMOTION:
                rect(screen, (0, 0, 0), (0, 0, 400, 400))
                snake = snake_move(snake, event.pos[0],event.pos[1])
                snake_draw(snake, screen)
                
    pygame.display.update()
