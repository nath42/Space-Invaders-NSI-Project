import pygame
from pygame.locals import QUIT
from librairie import fonctions as fct

pygame.init()

fenetre = pygame.display.set_mode((800,600))

main_loop_running = True

while main_loop_running == True:
    for event in pygame.event.get():
                if event.type == QUIT:
                     main_loop_running = False
    
    fct.lancement()


pygame.display.quit()
pygame.quit()