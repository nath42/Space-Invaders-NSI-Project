import pygame
from librairie import variables as var

pygame.init()

############################# FONCTIONS MENUS #################################

RUN=0
fenetre = pygame.display.set_mode((800,600))
vaisseau = var.vaisseau

## FONCTION AFFICHAGE DES BOUTONS DES MENUS
            
            #Boutons du menu principal
def boutons_principal():
    fenetre.fill( (50,50,50) )
    
    #création du bouton 1 Player
    bouton_1P = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((150, 300),(200, 75))
                     )
    
    text = var.police_menu.render('1 Player', False, (255,255,255))
    fenetre.blit(text, (195,325))
    
    #création du bouton 2 Players
    bouton_2P = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((450, 300),(200, 75))
                     )
    
    text = var.police_menu.render('2 Players', False, (255,255,255))
    fenetre.blit(text, (490,325))
    
    #création du bouton Crédits
    bouton_credits = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((150, 400),(200, 75))
                     )
    
    text = var.police_menu.render('Credits', False, (255,255,255))
    fenetre.blit(text, (195,425))
    
    #création du bouton Settings
    bouton_settings = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((450, 400),(200, 75))
                     )
    
    text = var.police_menu.render('Settings', False, (255,255,255))
    fenetre.blit(text, (490,425))
    
    gerer_principal(bouton_1P, bouton_2P, bouton_credits, bouton_settings)


            #Boutons du menu selection 1 Player
def boutons_selction_1P():
    fenetre.fill( (50,50,50) )
    bouton_play = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((450, 450),(300, 100))
                     )
    
    text = var.police_bouton_play.render('PLAY', False, (255,255,255))
    fenetre.blit(text, (510,470))
    
    bouton_back = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((20, 20),(150, 75))
                     )
    
    text = var.police_menu.render('Back', False, (255,255,255))
    fenetre.blit(text, (60,45))
    
    gerer_selction_1P(bouton_play, bouton_back)


            #Boutons du menu selection 2 Players
def boutons_selction_2P():
    fenetre.fill( (50,50,50) )
    bouton_play_2P = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((450, 450),(300, 100))
                     )
    
    text = var.police_bouton_play.render('PLAY', False, (255,255,255))
    fenetre.blit(text, (510,470))
    
    bouton_back = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((20, 20),(150, 75))
                     )
    
    text = var.police_menu.render('Back', False, (255,255,255))
    fenetre.blit(text, (60,45))
    
    gerer_selction_2P(bouton_play_2P, bouton_back)


            #Bouton du menu crédits
def bouton_credits():
    fenetre.fill( (50,50,50) )
    bouton_back = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((20, 20),(150, 75))
                     )
    
    text = var.police_menu.render('Back', False, (255,255,255))
    fenetre.blit(text, (60,45))
    
    gerer_credits(bouton_back)


            #Bouton du menu settings
def bouton_settings():
    fenetre.fill( (50,50,50) )
    bouton_back = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((20, 20),(150, 75))
                     )
    
    text = var.police_menu.render('Back', False, (255,255,255))
    fenetre.blit(text, (60,45))
    
    gerer_settings(bouton_back)




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




## RASSEMBLEMENT DES FONCTIONS POUR FAIRE TOURNER LE PROGRAMME DU MENU PRINCIPAL
def fonctions_principal():
    boutons_principal()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU SELECTION 1 PLAYER
def fonctions_selection_1P():
    boutons_selction_1P()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU SELECTION 2 PLAYERS
def fonctions_selection_2P():
    boutons_selction_2P()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU CREDITS
def fonctions_credits():
    bouton_credits()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DU MENU SETTINGS
def fonctions_settings():
    bouton_settings()




## RASSEMBLEMENT DES FONCTIONS POUR TOURNER LE PROGRAMME DE L'INTERFACE DU JEU
def fonctions_jeu():
    affichage_jeu()









#################################### FONCTIONS JEU ###################################
    
def vaisseau_control(event, vaisseau, pressed_left, pressed_right):
    if event.type == pygame.KEYDOWN:
            
        if event.key == pygame.K_LEFT:
            pressed_left = True
        elif event.key == pygame.K_RIGHT:
            pressed_right = True

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            pressed_left = False
        elif event.key == pygame.K_RIGHT:
            pressed_right = False
            
    return pressed_left, pressed_right




def gameplay():
    for event in pygame.event.get():
        v_en_mouv = vaisseau_control(event, vaisseau, pressed_left=False, pressed_right=False)
    
        if v_en_mouv[0] == True:
            vaisseau.position[0] -= 15
        if v_en_mouv[1] == True:
            vaisseau.position[0] += 15




def dynamic_background():
    
    var.background_pos += 3
    if var.background_pos !=0:
        var.background_bis = var.background
    
    var.background_bis_pos += 3
    if var.background_bis_pos > 0:
        var.background_pos = 0
        var.background_bis_pos = -600
        
    fenetre.blit(var.background, (0, var.background_pos))
    fenetre.blit(var.background_bis, (0, var.background_bis_pos))



def affichage_jeu():   
    
    dynamic_background()
    gameplay()
    
    vaisseau_sprite = pygame.image.load(vaisseau.url_image).convert()
    fenetre.blit(vaisseau_sprite, vaisseau.position)
    
    pygame.display.flip()
    








################################### LANCEMENT DU JEU ###################################

def lancement():
             
        if RUN==0:
            fonctions_principal()
            pygame.display.flip()
         
        if RUN==1:
            #print(RUN)
            fonctions_selection_1P()
            pygame.display.flip()
            
        if RUN==2:
            fonctions_selection_2P()
            pygame.display.flip()
            
        if RUN==3:
            fonctions_credits()
            pygame.display.flip()
            
        if RUN==4:
            fonctions_settings()
            pygame.display.flip()
            
        if RUN==777:
            #print(RUN)
            fonctions_jeu()
            pygame.display.flip()