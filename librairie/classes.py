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
        n=1
        # if fonction_time(durée)
        
        v.movspeed = v.movspeed = 0.2




class Ennemis:
    
      def __init__(self, pv, muni, x, y, vitesse, acceler, shotspeed, force):
        self.vie = pv
        self.muni = muni
        self.vitesse = vitesse
        self.acceler = acceler # Ennemis plus forts, donc plus tard...
        self.shotspeed = shotspeed
        self.force = force
        
      def affichepv_en(self): #Affiche les nombres de vie
        return self.vie
      # Pas utile pour les premiers ennemis (plus faibles)
      # Mais utile pour les boss avec le point de vie affiché 
    
      def attaque(self,cible):
        cible.vie = cible.vie-self.force