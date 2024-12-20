import pygame
from pygame.draw import *
from random import randint
from rgbhsl import intRGB
from snakesss import snake_move, snake_draw, dead, dead, snake0
from snakesss import snake
from fooddd import iffood, food0, drawfood
from fooddd import food

from startgame import *
from gameover import *

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

    if GAME_STAGE == "Menu": 
        #Окно "Меню"
        #Обновляет данные еды и змейки до стартовых. Рисует начальный экран. Реагирует на клики.
        food0(food)
        snake0(snake)
        ####
        screen.blit(menuscreen(), (0, 0))
        ### 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                GAME_STAGE = "Exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                xmouse = event.pos[0]
                ymouse = event.pos[1]
                GAME_STAGE = "Game"

    if GAME_STAGE == "Game": #Окно самой игры
        #Перемещает змейку. Проверяет еду и условия "смерти"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_STAGE = "Exit"
            if event.type == pygame.MOUSEMOTION:
                xmouse = event.pos[0]
                ymouse = event.pos[1]

        rect(screen, (255, 255, 255), (0, 0, 400, 400))
        snake_move(snake, xmouse, ymouse)
        snake_draw(snake, screen)
        drawfood(food, screen)
        ###
        if dead(snake):
            GAME_STAGE = "Game over"
        iffood(snake, food)


        

    if GAME_STAGE == "Game over": #Окно Смерти
        #Рисует финальный экран. Реагирует на клики. 
        screen.blit(game_over(('Score: '+ str(snake.score))), (0, 0))
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                GAME_STAGE = "Exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                GAME_STAGE = "Menu"
        
        
                
    pygame.display.update()
