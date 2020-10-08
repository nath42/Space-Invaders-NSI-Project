import pygame
from pygame.locals import QUIT
from librairie import fonctions as fct
from librairie import variables as var

pygame.init()
pygame.key.set_repeat(10,10)
fenetre = pygame.display.set_mode((800,600))
vaisseau = var.vaisseau

running = True
while running == True:
        
    fct.lancement()
    
    for event in pygame.event.get():
            #print('check')
            
            fct.gameplay(event)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                fct.tirer_bullet()
                #print("touche pressée : TIRER")

            if event.type == QUIT:
                        print("On ferme !")
                        running = False
                        
            
                    
pygame.display.quit()
pygame.quit()