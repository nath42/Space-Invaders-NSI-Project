# Fichier des classes du projet Space Invaders NSI 

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

    def mouvement(acceleration):
      vx , vy = vitesse
      ax , ay = acceleration
      vitesse = (vx+ax , vy+ay)
      return vitesse
      
player1=Vaisseau(0, 100, 50, 2, 2, 0)
player2=Vaisseau(0, 100, 50, 2, 2, 0)

class Ennemis:
      def __init__(self, pv, muni, x, y, vitesse, acceler, shotspeed, force):
        self.vie=pv
        self.muni=muni
        self.vitesse=vitesse
        self.acceler=acceler # Ennemis plus forts, donc plus tard...
        self.shotspeed=shotspeed
        self.force=force
      def affichepv_en(self): #Affiche les nombres de vie
        return self.vie
      def attaque(self,cible):
        cible.vie=cible.vie-self.force
# Pas utile pour les premiers ennemis (plus faibles)
# Mais utile pour les boss avec le point de vie affiché     
niv1=Ennemis(1, 100, 0, 0, 5, 0, 1, 2)    # Couleur gris
niv2=Ennemis(10, 100, 0, 0, 5, 0, 1.1, 4)  # Couleur Vert
niv3=Ennemis(20, 100, 0, 0, 5, 0, 1.2, 6)  # Couleur bleu
niv4=Ennemis(30, 100, 0, 0, 5, 0, 1.4, 8)  # Couleur violet
niv5=Ennemis(50, 100, 0, 0, 5, 0, 1.6, 15)  # Couleur rouge