import pygame
from pygame.draw import *
pygame.init()

#цвета
weiß=(225,225,225)
blau = (34, 103, 242)
schwarc = (0, 0, 0)
orange=(250, 120, 65)
dunkelblau= (14,31,115)

Überschrift = pygame.font.SysFont(pygame.font.get_default_font(), 40)
Grundtext = pygame.font.SysFont(pygame.font.get_default_font(), 25)

def menuscreen():
    Menü = pygame.Surface((400,400))
    Menü.fill(weiß)
    
    #вывод текста
    guten_morgen = Überschrift.render("Змейка", True, (orange))
    Menü.blit(guten_morgen, (140, 150))
    
    gemacht = Grundtext.render("made by:",True, (orange))
    Menü.blit(gemacht, (150, 200))
    
    name = Grundtext.render("Барышни",True, (orange))
    Menü.blit(name, (147, 219))
    
    
#рисует цветочек
    circle(Menü, (dunkelblau),(200,285),15)
    circle(Menü, (dunkelblau),(170,285),15)
    circle(Menü, (dunkelblau),(160,297),15)
    circle(Menü, (dunkelblau),(210,297),15)
    circle(Menü, (dunkelblau),(210,315),15)
    circle(Menü, (dunkelblau),(160,315),15)
    circle(Menü, (dunkelblau),(175,330),15)
    circle(Menü, (dunkelblau),(200,330),15)
    circle(Menü, (blau), (185, 300), 30)
    circle(Menü, (dunkelblau),(185,275),10 )
    circle(Menü, (weiß),(185,275),5)
    circle(Menü, (weiß),(175,320),3)
    circle(Menü, (weiß),(197,320),3)
    circle(Menü, (weiß),(160,305),3)
    circle(Menü, (weiß),(210,305),3)
    circle(Menü, (weiß),(206,290),3)
    circle(Menü, (weiß),(165,290),3)
    
    #рисует кружочки по краям
    circle(Menü, (blau), (400, 0), 100)
    
    circle(Menü, (blau), (0, 400), 70)
    
    return Menü

#FPS = 30
#screen = pygame.display.set_mode((400, 400))


#screen.blit(menuscreen(), (0, 0))
#pygame.display.update()
#clock = pygame.time.Clock()
#finished = False

#while not finished:
    #clock.tick(FPS)
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
           #finished = True

#pygame.quit()