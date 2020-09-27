import pygame
from pygame.locals import * # import des constantes inclu dans la librarie pygame
pygame.init()

 
fenetre = pygame.display.set_mode((800,600))
myfont = pygame.font.SysFont('Helvetic', 40)
pourQuitter = True


def fonction_stop():
    global pourQuitter # la valeur pourQuitter deviens universel au programme
    for event in pygame.event.get(): # On parcours la liste de tous les événements reçus
        if event.type == QUIT: # Si un de ces événements est de type QUIT (QUIT fais parti des constantes de pygame)
            pourQuitter = False # On change la valeur pourQuitter qui intervient aussi dans boucle_principale




## FONCTION AFFICHAGE MENUS
def menu_P1():
    #global color_P1 
    pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((150, 300),(200, 75))
                     )
    
    text = myfont.render('1 Player', False, (255,255,255))
    fenetre.blit(text, (200,325))
    
    gerer_menu_P1()
    
    
def menu_P2():
    #global color_P2
    pygame.draw.rect(fenetre,
                     (190,0,30),
                     pygame.Rect((450, 300),(200, 75))
                     )
    
    text = myfont.render('2 Player', False, (255,255,255))
    fenetre.blit(text, (500,325))
    
    gerer_menu_P2()
    
    
def menu_credit():
    #global color_credit 
    pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((150, 350),(200, 75))
                     )
    
    text = myfont.render('Credit', False, (255,255,255))
    fenetre.blit(text, (200,375))
    
    gerer_menu_credit()
    
    
def menu_settings():
    #global color_settings 
    pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect((450, 350),(200, 75))
                     )
    
    text = myfont.render('Settings', False, (255,255,255))
    fenetre.blit(text, (500,375))
    
    gerer_menu_settings()



## FONCTIONS POUR GERER QUEL MENU SE LANCE SI J'APPUYE SUR UNE TOUCHE
def gerer_menu_P1():
    
    # global color_P1
    # global color_P2
    # global color_credit
    # global color_settings
    
    global afficher
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_RIGHT:
                    # color_P1=(120,120,120)
                    # color_P2=(190,0,30)
                    # color_credit=(120,120,120)
                    # color_settings=(120,120,120)
                    afficher = menu_P2
                    
                if event.key == K_DOWN:
                    # color_P1=(120,120,120)
                    # color_P2=(120,120,120)
                    # color_credit=(190,0,30)
                    # color_settings=(120,120,120)
                    afficher = menu_credit

def gerer_menu_P2():
    
    # global color_P1
    # global color_P2
    # global color_credit
    # global color_settings
    
    global afficher
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_LEFT:
                    # color_P1=(190,0,30)
                    # color_P2=(120,120,120)
                    # color_credit=(120,120,120)
                    # color_settings=(120,120,120)
                    afficher = menu_P1
                
                if event.key == K_DOWN:
                    # color_P1=(120,120,120)
                    # color_P2=(120,120,120)
                    # color_credit=(120,120,120)
                    # color_settings=(190,0,30)
                    afficher = menu_settings

def gerer_menu_credit():
    
    # global color_P1
    # global color_P2
    # global color_credit
    # global color_settings
    
    global afficher
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_RIGHT:
                    # color_P1=(120,120,120)
                    # color_P2=(120,120,120)
                    # color_credit=(120,120,120)
                    # color_settings=(190,0,30)
                    afficher = menu_settings
                    
                if event.key == K_UP:
                    # color_P1=(190,0,30)
                    # color_P2=(120,120,120)
                    # color_credit=(120,120,120)
                    # color_settings=(120,120,120)
                    afficher = menu_P1

def gerer_menu_settings():
    
    # global color_P1
    # global color_P2
    # global color_credit
    # global color_settings
    
    global afficher
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_LEFT:    
                    # color_P1=(120,120,120)
                    # color_P2=(120,120,120)
                    # color_credit=(190,0,30)
                    # color_settings=(120,120,120)
                    afficher = menu_credit
                    
                if event.key == K_UP:
                    # color_P1=(120,120,120)
                    # color_P2=(190,0,30)
                    # color_credit=(120,120,120)
                    # color_settings=(120,120,120)
                    afficher = menu_P2


# ##SET UP INITIALE (AU LANCEMENT DU PROGRAMME)
# color_P1=(190,0,30)
# color_P2=(120,120,120)
# color_credit=(120,120,120)
# color_settings=(120,120,120)

afficher = menu_P1


## BOUCLE POUR FAIRE TOURNER LE PROGRAMME
def boucle_principale():
    while pourQuitter:
        fenetre.fill( (0,0,0) )
        
        fonction_stop()
         
        # Exécute la fonction affectée à afficher (Player 1 / Player 2 /...)
        afficher()
         
         
        pygame.display.update()
         
    pygame.quit()

    
boucle_principale()