from rgbhsl import intRGB
from pygame.draw import *

x = [0, 10, 20, 30]
y = [0, 10, 20, 30]
H = [0, 10, 20, 30]

snake = x, y, H


def snake_move(snake, mx, my): #отвечает за перемещение мышки в заданные координаты
    x, y, H = snake
    nstep = 5
    rx = - x[0] + mx
    ry = - y[0] + my
    step = ((rx**2 + ry**2)**0.5)/nstep
    x = [(x[0] + rx/step)] + x
    x.pop()
    y = [(y[0] + ry / step)] + y
    y.pop()
    H = [(H [0] + 10) % 360] + H
    H.pop()
    return x, y, H

def snake_draw(snake, screen):
    x, y, H = snake
    for i in range(0, len(x)- 1):
        circle(screen, intRGB(H[i]), (x[i], y[i]), 5)

def snake_long(snake, n):
    x, y, H = snake
    if n > 0:
        for i in range(n):
            x = [x[0]] + x
            y = [y[0]] + y
            H = [H[0]] + H
    elif n < 0:
        for i in range(abs(n)):
            x.pop()
            y.pop()
            H.pop()