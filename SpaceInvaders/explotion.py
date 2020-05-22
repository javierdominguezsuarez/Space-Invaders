class Explotion (sprite.Sprite):

    def __init__(self,coord,tipe):
        """Método que inicia el objeto"""
        super().__init__()
        #Si es de alien
        if tipe == 0 :
            try :
                #Extraenos la imagen para la explosión
                self.image = image.load(GenericData.AL_PATH +"explosion.png")
            except FileNotFoundError :
                print("Error en el sprite de la explosión")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
            self.rect.centerx = coord[0]
            self.rect.centery = coord[1]
        #Si es de la nave
        elif tipe == 1 :
            try :
                #Extraenos la imagen para la explosión
                self.image = image.load(GenericData.IMG_PATH +"explosion_ship1.png")
            except FileNotFoundError :
                print("Error en el sprite de la explosión")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
            self.rect.centerx = coord[0]
            self.rect.centery = coord[1]
        elif tipe == 2:
            try :
                #Extraenos la imagen para la explosión
                self.image = image.load(GenericData.AL_PATH +"explosion_tocho.png")
            except FileNotFoundError :
                print("Error en el sprite de la explosión")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
            self.rect.centerx = 1400#coord[0]
            self.rect.centery = 1200#coord[1]+40
        
        
        #Reloj para controlar el tiempo que se emite
        self.clk = time.get_ticks()
        
        
        
    def update(self):
        """Método para controlar la explosión"""
        #Dejamos un tiempo y eliminamos el objeto
        if (time.get_ticks() - self.clk) > 70 :
            self.kill()
