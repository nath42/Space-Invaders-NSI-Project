import pygame
from librairie import classes as cl

pygame.init()

######################### VAR POUR FONCTIONNALITE MENU #############################

police_menu = pygame.font.SysFont('Helvetic', 40)
police_bouton_play = pygame.font.SysFont('Helvetic', 100)
pourQuiter=True
RUN=0







######################## VAR POUR FONCTIONNALITE JEU ##############################

#Paramètres classe vaisseau Player 1
position = [400, 500]
pv = 100
muni = 50
coefv = 1
shotspeed = 1
url_image = "assets/vaisseau.jpg"

vaisseau = cl.Vaisseau (position, pv, muni, coefv, shotspeed, url_image)

#Paramètres affichage
background = pygame.image.load("assets/background.png")
background_pos = 0
background_bis_pos = -600





######################## VAR DE CLASSES DEFINIES #########################################

#Paramètres classe ennemis par niveau
niv1 = cl.Ennemis (1, 100, 0, 0, 5, 0, 1, 2)    # Couleur gris
niv2 = cl.Ennemis (10, 100, 0, 0, 5, 0, 1.1, 4)  # Couleur Vert
niv3 = cl.Ennemis (20, 100, 0, 0, 5, 0, 1.2, 6)  # Couleur bleu
niv4 = cl.Ennemis (30, 100, 0, 0, 5, 0, 1.4, 8)  # Couleur violet
niv5 = cl.Ennemis (50, 100, 0, 0, 5, 0, 1.6, 15)  # Couleur rouge