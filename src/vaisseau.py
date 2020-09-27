# -*- coding: utf-8 -*-
#fichier éxécutant la fenêtre de jeu 

#importations classes/fonctions :
import sys
path = "./"
sys.path.append(path)
from classes import *
from game_func import *

#importations modules :
import pygame
from pygame.locals import *

def Game_Interface():

    #Paramètres classe vaisseau Player 1
    position = [300, 400]
    pv = 100
    muni = 50
    coefv = 1
    shotspeed = 1
    urlimage = "././assets/vaisseau.jpg"

    vaisseau=Vaisseau(position, pv, muni, coefv, shotspeed, urlimage)


    #Initialisation de l'affichage
    pygame.init
    ecran = pygame.display.set_mode((0,0),FULLSCREEN)
    bg = pygame.image.load("././assets/bg.png")
    bg_y = 0
    bg_y2 = -1080

    #import et initialisation du vaisseau
    Vobjet = pygame.image.load(vaisseau.urlimage).convert()
    ecran.blit(Vobjet, vaisseau.position)
    posx = 0
    pressed_left = False
    pressed_right = False

    #Rafraichissement
    pygame.display.flip()



    # Game Loop
    continuer = True
    while continuer == True:
        for event in pygame.event.get():
            #fermage de la fenetre, bug a résoudre later...
            v = vaisseau_control(event, vaisseau, pressed_left=False, pressed_right=False)
        if v[0] == True:
            vaisseau.position[0] += 15
        if v[1] == True:
            vaisseau.position[0] -= 15
        
        dynamic_bg()


        ecran.blit(Vobjet, vaisseau.position)
        pygame.display.flip()

        
