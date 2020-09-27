# Fichier des classes du projet Space Invaders NSI 
import pygame

class Vaisseau:
  def __init__(self, position:float, pv, muni, coefv, shotspeed, urlimage):
    self.vie=pv
    self.muni=muni
    self.coefv=coefv
    self.shotspeed=shotspeed
    self.position= position
    self.urlimage = urlimage
    
  def affichepv(self): #Affiche les nombres de vie
    return self.vie

  def add_hp(self, player, hp):
    player.vie = player.vie + hp 

  def affichemuni(self): #Affiche le nombre de munitions
    return self.muni

  def add_bullets(self, player, bullet):
    player.muni = player.muni + bullet
  # Fonction enlevé munition est à faire avec pygame...
  def rechargemuni(self): # Recharge les munitions
      #TEMPS DE RECHARGE. PTITE ANIMATION 3SEC..
    if self.muni==0:
      nbrmuni=50 
    self.muni=self.muni+nbrmuni

  def shield(self):
    self.vie=self.vie+3

  def boost(self, v):
    # if fonction_time(durée)
        
    v.movspeed = v.movspeed = 0.2

  def deplacement(self, x):
    self.position += x
    

