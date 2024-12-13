from random import randint
from pygame.draw import *
from snakesss import snake_long

class food:
    x = []
    y = []
    n = 5

def food0(food):
    food.x = []
    food.y = []
    for i in range (0, food.n):
        food.x = food.x + [randint(20,350)]
        food.y = food.y + [randint(20,350)]
    
    

def drawfood(food, screen):
    for i in range (0, food.n):
        circle(screen, (100, 200, 10), (food.x[i], food.y[i]), 5)




def iffood(snake, food):
    for i in range (0, food.n):
        if (snake.x[0] - food.x[i])**2 + (snake.y[0] - food.y[i])**2 < 40:
            food.x[i] = randint(20,350)
            food.y[i] = randint(20,350)
            snake_long(snake, 3)



            
        
