import pygame

from librairie import variables as var
from librairie import classes as cl

pygame.init()

############################# FONCTIONS MENUS #################################


RUN=0
fenetre = pygame.display.set_mode((800,600))
vaisseau = var.vaisseau
ennemis = var.niv1

## FONCTIONS POUR GERER QUEL MENU SE LANCE SI J'APPUYE SUR UNE TOUCHE

            #Menu Principal
def gerer_principal(bouton_1P, bouton_2P, bouton_credits, bouton_settings):
    global RUN
    
    mouse = pygame.mouse.get_pressed()
    #print(mouse[0]) 
    if mouse[0] == True:
        mouse_position = pygame.mouse.get_pos()
         
        if bouton_1P.collidepoint(mouse_position):
                    RUN=1
                    #print(RUN)
        if bouton_2P.collidepoint(mouse_position):
                    RUN=2
                    #print(RUN)
        if bouton_credits.collidepoint(mouse_position):
                    RUN=3
                    #print(RUN)
        if bouton_settings.collidepoint(mouse_position):
                    RUN=4
                    #print(RUN)

        
            #Menu selection 1 Player
def gerer_selction_1P(bouton_play, bouton_retour):
    global RUN
    
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == True:
        #print("oui")
        mouse_position = pygame.mouse.get_pos()
        
        if bouton_play.collidepoint(mouse_position):
                    RUN=777
                    #print(RUN)
        if bouton_retour.collidepoint(mouse_position):
                    RUN=0
                    #print(RUN)


            #Menu selection 2 Players
def gerer_selction_2P(bouton_play_2P, bouton_back):
    global RUN
    
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == True:
        #print("oui")
        mouse_position = pygame.mouse.get_pos()
        
        if bouton_play_2P.collidepoint(mouse_position):
                    RUN=777
                    #print(RUN)
        if bouton_back.collidepoint(mouse_position):
                    RUN=0
                    #print(RUN)


            #Menu crédits
def gerer_credits(bouton_back):
    global RUN
    
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == True:
        #print("oui")
        mouse_position = pygame.mouse.get_pos()
        
        if bouton_back.collidepoint(mouse_position):
                    RUN=0
                    #print(RUN)


            #Menu settings
def gerer_settings(bouton_back):
    global RUN
    
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == True:
        #print("oui")
        mouse_position = pygame.mouse.get_pos()
        
        if bouton_back.collidepoint(mouse_position):
                    RUN=0
                    #print(RUN)





## FONCTION AFFICHAGE DES BOUTONS DES MENUS
            
            #Boutons du menu principal
def boutons_principal():
    
    #création du bouton 1 Player
    bouton_1P = cl.boutons((200, 75),(150, 300),'1 Player',var.police_menu,(195,325)).creation()
    
    #création du bouton 2 Players
    bouton_2P = cl.boutons((200, 75),(450, 300),' 2 Players',var.police_menu,(490,325)).creation()

    #création du bouton Crédits
    bouton_credits = cl.boutons((200, 75),(150, 400),'Credits',var.police_menu,(195,425)).creation()
    
    #création du bouton Settings
    bouton_settings = cl.boutons((200, 75),(450, 400),'Settings',var.police_menu,(490,425)).creation()
    
    
    gerer_principal(bouton_1P, bouton_2P, bouton_credits, bouton_settings)


            #Boutons du menu selection 1 Player
def boutons_selction_1P():
    
    #création du bouton PLAY
    bouton_play = cl.boutons((300, 100),(450, 450),'PLAY',var.police_bouton_play,(510,470)).creation()
    
    #création du bouton Back
    bouton_back = cl.boutons((150, 75),(20, 20),'Back',var.police_menu,(60,45)).creation()
    
    
    gerer_selction_1P(bouton_play, bouton_back)


            #Boutons du menu selection 2 Players
def boutons_selction_2P():
    
    #création du bouton PLAY
    bouton_play_2P = cl.boutons((300, 100),(450, 450),'PLAY',var.police_bouton_play,(510,470)).creation()
    
    #création du bouton Back
    bouton_back = cl.boutons((150, 75),(20, 20),'Back',var.police_menu,(60,45)).creation()
    
    
    gerer_selction_2P(bouton_play_2P, bouton_back)


            #Bouton du menu crédits
def bouton_credits():
    
    #création du bouton Back
    bouton_back = cl.boutons((150, 75),(20, 20),'Back',var.police_menu,(60,45)).creation()
    
    
    gerer_credits(bouton_back)


            #Bouton du menu settings
def bouton_settings():
    
    #création du bouton Back
    bouton_back = cl.boutons((150, 75),(20, 20),'Back',var.police_menu,(60,45)).creation()
    
    
    gerer_settings(bouton_back)





## RASSEMBLEMENT DES FONCTIONS POUR FAIRE TOURNER LE PROGRAMME DU MENU PRINCIPAL
def fonctions_principal():
    dynamic_background()
    boutons_principal()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU SELECTION 1 PLAYER
def fonctions_selection_1P():
    dynamic_background()
    boutons_selction_1P()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU SELECTION 2 PLAYERS
def fonctions_selection_2P():
    dynamic_background()
    boutons_selction_2P()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU CREDITS
def fonctions_credits():
    dynamic_background()
    bouton_credits()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU SETTINGS
def fonctions_settings():
    dynamic_background()
    bouton_settings()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DE L'INTERFACE DU JEU
def fonctions_jeu():
    dynamic_background()
    affichage_jeu()









#################################### FONCTIONS JEU ###################################


def affichage_bullet():
    v = pygame.image.load(var.bullet_vaisseau.url_image).convert()
    fenetre.blit(v, var.bullet_vaisseau.position_initial)



def tirer_bullet():
    
    affichage_bullet()
  

def dynamic_background():
    """
    var.background_pos += 3
    if var.background_pos !=0:
        var.background_bis = var.background
    
    var.background_bis_pos += 3
    if var.background_bis_pos > 0:
        var.background_pos = 0
        var.background_bis_pos = -600
        """
    fenetre.blit(var.background, (0, var.background_pos))
     #fenetre.blit(var.background_bis, (0, var.background_bis_pos))
    



def gameplay(event):
    #print("attente de la pression d'une touche")
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            vaisseau.position[0] -= vaisseau.coefv
            #print("touche pressée : gauche oui, droite non")
        
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            vaisseau.position[0] += vaisseau.coefv
            #print("touche pressée : droite oui, gauche non")
            
def ajout_ennemi(liste_ennemi, url_image, taux_apparition=100, pv=3, muni=0, vitesse=15, shotspeed=0, force=10):
	"""preconditions: la liste contenant les objets vaisseaux, les caractéristiques du vaisseau a ajouter"""
	aleatoire_apparition=randint(1,taux_apparition)
	if aleatoire_apparition == 1:
		x=randint(0,800)
		
		liste_ennemi.append(cl.Ennemis(pv, muni, x, vitesse, shotspeed, force, url_image))
		return liste_ennemi

	return liste_ennemi



def collision(liste_collision,liste_objet):
	if vaisseau.collidelist(liste_collision) == -1:
		liste_objet=liste_objet[1:]

def disparition(liste_objet):
	return liste_objet[1:]






def affichage_jeu():   
    
    dynamic_background()
    
    vaisseau_sprite = pygame.image.load(vaisseau.url_image).convert()
    fenetre.blit(vaisseau_sprite, vaisseau.position)
    
    # ennemis_sprite = pygame.image.load(ennemis.url_image).convert()
    # fenetre.blit(ennemis_sprite, mouvement_ennemis())
    
    pygame.display.flip()
    








################################### LANCEMENT DU JEU ###################################

def lancement():
    #print("running fct lancement")
    
    if RUN==0:
        fonctions_principal()
        #print("running fct principal")
        pygame.display.flip()
     
    if RUN==1:
        fonctions_selection_1P()
        #print("running fct selection 1P")
        pygame.display.flip()
        
    if RUN==2:
        fonctions_selection_2P()
        #print("running fct selction 2P")
        pygame.display.flip()
        
    if RUN==3:
        fonctions_credits()
        #print("running fct credits")
        pygame.display.flip()
        
    if RUN==4:
        fonctions_settings()
        #print("running fct settings")
        pygame.display.flip()
        
    if RUN==777:
        fonctions_jeu()
        #print("running fct jeu")
        pygame.display.flip()
    