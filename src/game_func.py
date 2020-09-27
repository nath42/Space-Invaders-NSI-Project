# -*- coding: utf-8 -*-
#Fichiers contenant des fonctions pygame
import pygame
from pygame.locals import *

ecran = pygame.display.set_mode((0,0),FULLSCREEN)
bg = pygame.image.load("././assets/bg.png")
bg_y = 0
bg_y2 = -1080

def close_screen(event):
    pass
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("flag")
            continuer = True
            return continuer
        else:
            continuer = True
            return continuer
        
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

def dynamic_bg():
    
    global bg_y
    global bg_y2
    global bg
    global ecran

    bg_y += 5
    if bg_y !=0:
        bg2 = bg
    bg_y2 += 5
    if bg_y2 > 0:
        bg_y = 0
        bg_y2 = -1080
    
    ecran.blit(bg2, (0, bg_y2))
    ecran.blit(bg, (0, bg_y))

    return [bg_y, bg_y2, bg, bg2, ecran]


    