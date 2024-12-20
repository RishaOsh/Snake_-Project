import pygame 
from pygame.draw import * 
pygame.init()

Letras = pygame.font.SysFont(pygame.font.get_default_font(), 60) # шрифт

def game_over(puntuaje):
     juego = pygame.Surface((400,400))
     blanco = (255,255,255)
     juego.fill (blanco)

     letritas = Letras.render("GAME OVER", True, (245, 70, 50)) #вывод текста 
     juego.blit(letritas, (80, 170))

     rectangulo = Letras.render(str(puntuaje), True, (245, 70, 50)) # вывод очков
     juego.blit(rectangulo, (70,250))

     # Дизайн
     circle(juego, (245, 70, 50), (50, 70), 80)  
     circle(juego, (38, 174, 160), (50, 70), 40) 
     circle(juego, (38, 174, 160), (10, 142), 14)
     circle(juego, (38, 174, 160), (65, 145), 14)
     circle(juego, (38, 174, 160), (117, 115), 14)
     circle(juego, (38, 174, 160), (130, 59), 14)
     circle(juego, (38, 174, 160), (104, 8), 14)
     circle(juego, (223, 121, 8), (345, 345), 80, 34)
     circle(juego, (253, 217, 26), (345, 345), 35)
     polygon (juego, (255, 8, 13), [(345,333), (355,345), (345,358), (335,345)], 5)
     line (juego,(255, 8, 13),(345,333),(345,265), 5)
     line (juego,(255, 8, 13),(355,345),(400,345), 5)
     line (juego,(255, 8, 13),(345,358),(345,400), 5)
     line (juego,(255, 8, 13),(335,345),(265,345), 5)     
     line (juego,(0,0,0),(80,50),(20,87), 8) 
     line (juego,(0,0,0),(67,37),(13,70), 8) 
     line (juego,(0,0,0),(87,68),(34,101), 8)
      
     return juego

#FPS = 30
#screen = pygame.display.set_mode((400, 400))

#screen.blit(game_over(8), (0, 0))
#pygame.display.update()
#clock = pygame.time.Clock()
#finished = False

#while not finished:
    #clock.tick(FPS)
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #finished = True
#pygame.quit()