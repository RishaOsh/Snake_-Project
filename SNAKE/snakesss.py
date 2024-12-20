from rgbhsl import intRGB
from pygame.draw import *

#Переменные змейки координты x y и цвет H
class snake:
    x = [15, 12, 9, 6, 3]
    y = [15, 12, 9, 6, 3]
    H = [0, 10, 20, 30, 40]
    score = 0


def snake0(snake): #приведние змейки в стартовое состояние
    snake.x = [15, 12, 9, 6, 3]
    snake.y = [15, 12, 9, 6, 3]
    snake.H = [0, 10, 20, 30, 40]
    snake.score = 0 



def snake_move(snake, mx, my): #отвечает за перемещение мышки в заданные координаты
    nstep = 4
    rx = - snake.x[0] + mx
    ry = - snake.y[0] + my
    step = ((rx**2 + ry**2)**0.5)/nstep
    snake.x = [(snake.x[0] + rx/step)] + snake.x
    snake.x.pop()
    snake.y = [(snake.y[0] + ry / step)] + snake.y
    snake.y.pop()
    snake.H = [(snake.H [0] + 10) % 360] + snake.H
    snake.H.pop()


def snake_draw(snake, screen): #отображение змейки
    for i in range(0, len(snake.x)- 1):
        circle(screen, intRGB(snake.H[i]), (snake.x[i], snake.y[i]), 5)

def snake_long(snake, n): #увеличивать или умеьшать линну змейки
    if n > 0:
        for i in range(n):
            snake.x = [snake.x[0]] + snake.x
            snake.y = [snake.y[0]] + snake.y
            snake.H = [snake.H[0]] + snake.H
    elif n < 0:
        for i in range(abs(n)):
            snake.x.pop()
            snake.y.pop()
            snake.H.pop()

def dead(snake):
    ret = False
    for i in range(2, len(snake.x)):
        if (snake.x[i] - snake.x[0])**2 + (snake.y[i] - snake.y[0])**2 < 5:
            ret = True
    if (snake.x[0] > 400) or (snake.x[0] < 0) or (snake.y[0] > 400) or (snake.y[0] < 0): 
        ret = True       
    return ret