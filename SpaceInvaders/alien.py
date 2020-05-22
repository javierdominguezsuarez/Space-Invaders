class Alien (sprite.Sprite):
    """Clase que define el comportamiento de un alien"""
    def __init__(self,speed):
        """Iniciamos el objeto"""
        #Iniciando la clase sprite
        super().__init__()
        
        try :
            #Extraenos la imagen para el sprite
            self.image = image.load(GenericData.AL_PATH +"alien.png")
        except FileNotFoundError :
            print("Sprite de alien no encontrado")
            
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        #Variable para controlar que se mueve izq o drc
        self.dir = 1

        #Velocidad
        assert type(speed) == int ,"Error de tipo en velocidad de alien"
        self.speed = speed
        self.top = 730
        #Atributos para guardar las coordenadas en la animación
        self.changex = 0
        self.changey = 0
        
    def update(self):
        """Método que define el movimiento """
        #Movimiento , de izquierda a derecha y cuando llegamos a una pared descendemos
        if self.rect.x < self.top :
            
            self.rect.x+= self.speed * self.dir
            
        elif self.rect.x > self.top:
            
            self.dir=-1
            self.rect.y +=13
            
        if self.rect.x > 3:
            
            self.rect.x+= self.speed * self.dir
            
        elif self.rect.x < 3:
            
            self.rect.y +=13
            self.dir=1
            
        #Si llegamos a la parte inferior eliminamos el objeto    
        if self.rect.y >=590:
            self.kill()

    #Getters y setters
    def changex (self):
        return self.changex
    def changex (self,n_changex):
        self.changex = n_changex
    def changey (self):
        return self.changey
    def changey (self,n_changey):
        self.changey = n_changey
    def dir (self):
        return self.dir
    def dir (self,n_dir):
        self.dir = n_dir
    def image (self):
        return self.image
    def image (self,n_image):
        self.image = n_image
    def rect (self):
        return self.rect
    def rect (self,n_rect):
        self.rect = n_rect
    def top (self):
        return self.top
    def top (self,n_top):
        self.top = n_top
    def speed (self):
        return self.speed
    def speed (self,n_speed):
        self.speed = n_speed
        
    def burn (self):
        """Método para proporiconar la información para la explosión"""
        #Atributos para guardar las coordenadas en la animación
        return (self.rect.centerx,self.rect.centery)
