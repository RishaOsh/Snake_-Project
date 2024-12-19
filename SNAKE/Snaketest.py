import pygame
from pygame.draw import *
pygame.init()   

#def и так далее.....

#это после твоей функции

FPS = 30
screen = pygame.display.set_mode((400, 400))
#screen.blit(#Называние функции#, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
##########
        if event.type == pygame.MOUSEBUTTONDOWN:
            print( event.pos[0], event.pos[1])
            circle(screen, (255,255,255), ( event.pos[0], event.pos[1]), 5)
            pygame.display.update()
###########

pygame.quit()