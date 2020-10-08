import pygame

pygame.init()
fenetre = pygame.display.set_mode((800,600))


class boutons:
    
    def __init__(self, taille, position_bouton, texte, police, position_texte):
        self.taille = taille
        self.position_bouton = position_bouton
        self.texte = texte
        self.police = police
        self.position_texte = position_texte
        
    def creation(self):
        bouton = pygame.draw.rect(
                     fenetre,
                     (190,0,30),
                     pygame.Rect(self.position_bouton, self.taille)
                     )
    
        info_ecrite = self.police.render(self.texte, False, (255,255,255))
        fenetre.blit(info_ecrite, self.position_texte)
        return bouton





class Vaisseau:
    
    def __init__(self, position:float, pv, muni, coefv, shotspeed, url_image):
        self.vie = pv
        self.muni = muni
        self.coefv = coefv
        self.shotspeed = shotspeed
        self.position = position
        self.url_image = url_image
    
    def affichepv(self): #Affiche les nombres de vie
        return self.vie

    def add_hp(self, hp):
        self.vie = self.vie + hp 

    def affichemuni(self): #Affiche le nombre de munitions
        return self.muni

    def add_bullets(self, bullet):
        self.muni = self.muni + bullet
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





class Ennemis:
    
      def __init__(self, pv, muni, x, vitesse, shotspeed, force, url_image):
        self.vie = pv
        self.muni = muni
				self.x = x
        self.vitesse = vitesse
        self.shotspeed = shotspeed
        self.force = force
				self.url_image = url_image
        
      def affichepv_en(self): #Affiche les nombres de vie
        return self.vie
      # Pas utile pour les premiers ennemis (plus faibles)
      # Mais utile pour les boss avec le point de vie affiché 
    
      def attaque(self,cible):
        cible.vie = cible.vie-self.force

			def afficher_ennemi(self):
				"""precondition: liste_ennemi [ennemi souhaité] """
				sprite = pygame.image.load(self.url_image).convert()
				fenetre.blit(sprite,(self.x,0))

			def deplacement_ennemi(self,ennemi_sprite):
				self.x+=self.vitesse
				self.afficher_ennemi()

class Bullet:
  
  def __init__(self, position_initial:list, coefv_bullet:int, url_image):
    self.position_initial = position_initial 
    self.coefv_bullet = coefv_bullet
    self.url_image = url_image
    
