class AlienTocho (Alien):
    """Clase para manejar aliens tochos"""
    def __init__(self,speed):
        """Método para iniciar el alien tocho"""
        super().__init__(speed)
        self.image = image.load(GenericData.AL_PATH +"alien_tocho.png")
        self.rect = self.image.get_rect()
        self.top = 570
