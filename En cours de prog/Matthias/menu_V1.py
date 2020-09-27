import pygame
from pygame.locals import * #import des constantes inclu dans la librarie pygame
pygame.init()



fenetre = pygame.display.set_mode((800,600))

        
def menuPrincipal_P1():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:    
                    menuPrincipal_P2()
                if event.key == K_DOWN:
                    menuPrincipal_credit()
            else:
                fenetre.blit(pygame.image.load("menuPrinc_P1.png").convert(),(0,0))
                pygame.display.flip()
                return menuPrincipal_P1()
        
def menuPrincipal_P2():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:    
                return menuPrincipal_P1()
            if event.key == K_DOWN:  
                return menuPrincipal_settings()
        else:
            fenetre.blit(pygame.image.load("menuPrinc_P2.png").convert(),(0,0))
            pygame.display.flip()
            return menuPrincipal_P2()

def menuPrincipal_settings():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT: 
                return menuPrincipal_credit()
            if event.key == K_UP:     
                return menuPrincipal_P2()
        else:
            fenetre.blit(pygame.image.load("menuPrinc_settings.png").convert(),(0,0))
            pygame.display.flip()
            return menuPrincipal_settings()

def menuPrincipal_credit():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:   
                return menuPrincipal_settings()
            if event.key == K_UP: 
                return menuPrincipal_P1()
        else:
            fenetre.blit(pygame.image.load("menuPrinc_credit.png").convert(),(0,0))
            pygame.display.flip()
            return menuPrincipal_credit()
        
def menuPrincipal(menu):
    while menu == True:
        menuPrincipal_P1()