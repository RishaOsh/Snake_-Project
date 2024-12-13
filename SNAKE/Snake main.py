import pygame
from pygame.draw import *
from random import randint
from rgbhsl import intRGB
from snakesss import snake_move, snake_draw, dead, snake_long, dead
from snakesss import snake, snake0
from fooddd import iffood, food0, drawfood
from fooddd import food
#from snakesss import *
from Menuscreen import *

global GAME_STAGE #Переменная отвечающая за этап игры "Menu" "Game" "Game over" "Exit"
GAME_STAGE = "Menu"

pygame.init()
FPS = 20
screen = pygame.display.set_mode((400, 400))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
# что-то со временем (?)

while not finished:
    clock.tick(FPS)
    if GAME_STAGE == "Exit": #Отвечает за сворачивание окна
        finished = True

    if GAME_STAGE == "Menu": #Окно "Меню"
        food0(food)
        snake0(snake)
        screen.blit(menu_screen_draw(), (0, 0)) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                GAME_STAGE = "Exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                xmouse = event.pos[0]
                ymouse = event.pos[1]
                GAME_STAGE = "Game"

    if GAME_STAGE == "Game": #Окно самой игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_STAGE = "Exit"
            if event.type == pygame.MOUSEMOTION:
                xmouse = event.pos[0]
                ymouse = event.pos[1]

        rect(screen, (0, 0, 0), (0, 0, 400, 400))
        snake_move(snake, xmouse, ymouse)
        snake_draw(snake, screen)
        drawfood(food, screen)

        if dead(snake):
            GAME_STAGE = "Game over"
        iffood(snake, food)


        

    if GAME_STAGE == "Game over": #Окно Смерти
        #screen.blit(menu_screen_draw(), (0, 0)) 
        snake_draw(snake, screen)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                GAME_STAGE = "Exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                xmouse = event.pos[0]
                ymouse = event.pos[1]
                GAME_STAGE = "Menu"
        
        
                
    pygame.display.update()
