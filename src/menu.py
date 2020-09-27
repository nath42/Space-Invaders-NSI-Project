import pygame
from pygame.locals import * # import des constantes inclues dans la librarie pygame

pygame.init()

#Import de le fonction Game_interface()
import sys
path = "./"
sys.path.append(path)
from vaisseau import *




## NECESSITES FONCTIONNELLES 
fenetre = pygame.display.set_mode((0,0),FULLSCREEN)
police_menu = pygame.font.SysFont('Helvetic', 40)
police_bouton_play = pygame.font.SysFont('Helvetic', 100)
pourQuitter = True
RUN=0




## FONCTION AFFICHAGE MENUS
            
            #Menu Principal
def boutons_principal():
    fenetre.fill( (50,50,50) )
    
    #création du bouton 1 Player
    bouton_1P = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((150, 300),(200, 75))
                     )
    
    text = police_menu.render('1 Player', False, (255,255,255))
    fenetre.blit(text, (195,325))
    
    #création du bouton 2 Players
    bouton_2P = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((450, 300),(200, 75))
                     )
    
    text = police_menu.render('2 Players', False, (255,255,255))
    fenetre.blit(text, (490,325))
    
    #création du bouton Crédits
    bouton_credits = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((150, 400),(200, 75))
                     )
    
    text = police_menu.render('Credits', False, (255,255,255))
    fenetre.blit(text, (195,425))
    
    gerer_principal(bouton_1P, bouton_2P, bouton_credits)
            
            #Menu selection 1 Player
def bouton_play():
    fenetre.fill( (50,50,50) )
    bouton_play = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((200, 300),(400, 100))
                     )
    
    text = police_bouton_play.render('PLAY', False, (255,255,255))
    fenetre.blit(text, (310,320))
    
    gerer_selction_1P(bouton_play)




## FONCTIONS POUR GERER QUEL MENU SE LANCE SI J'APPUYE SUR UNE TOUCHE

            #Menu Principal
def gerer_principal(bouton_1P, bouton_2P, bouton_credits):
    global RUN
    
    mouse = pygame.mouse.get_pressed()
    #print(mouse[0]) 
    if mouse[0] == True:
        mouse_position = pygame.mouse.get_pos()
         
        if bouton_1P.collidepoint(mouse_position):
                    RUN=1
                    print(RUN)
        if bouton_2P.collidepoint(mouse_position):
                    RUN=2
                    #print(RUN)
        if bouton_credits.collidepoint(mouse_position):
                    RUN=3
                    #print(RUN)
        
        mouse = False
        
            #Menu selection 1 Player
def gerer_selction_1P(bouton_play):
    global RUN
    
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == True:
        print("oui")
        mouse_position = pygame.mouse.get_pos()
        
        if bouton_play.collidepoint(mouse_position):
                    RUN=777
                    print(RUN)
        
        mouse = False


## RASSEMBLEMENT DES FONCTIONS POUR FAIRE TOURNER LE PROGRAMME DU MENU PRINCIPAL
def fonctions_principal():
    boutons_principal()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU SELECTION 1 PLAYER
def fonctions_selection_1P():
    bouton_play()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DE L'INTERFACE DU JEU
def fonctions_jeu():
    Game_Interface()




## LANCEMENT DU PROGRAMME
def lancement():
    global pourQuitter
    
    while pourQuitter:
        for event in pygame.event.get():
                if event.type == QUIT:
                     pourQuitter = False
                     
        if RUN==0:
            fonctions_principal()
            pygame.display.flip()
         
        if RUN==1:
            #print(RUN)
            fonctions_selection_1P()
            pygame.display.flip()
            
        if RUN==777:
            #print(RUN)
            fonctions_jeu()
            pygame.display.flip()

    pygame.display.quit()
    pygame.quit()


lancement()

