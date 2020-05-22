class Wall (sprite.Sprite):
    """Clase que define el comportamiento de un muro"""
    
    def __init__(self,coord_x,coord_y,row,column,color_enable):
        
        super().__init__()

        
        #La variable color_enable, dependiendo de si se encuentra en la primera o última fila lo pinta de un color u otro
        self.color = color_enable

        #Creamos los rectángulos que forman los muros
        self.image = Surface((10,10))
        if self.color == 0 :
            self.image.fill((46,139,87))
        else :
            self.image.fill((67,205,128))
            
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        
        #Obtenemos las coordenadas del rectángulo
        self.rect.x=coord_x
        self.rect.y=coord_y
        
        #Obtenemos su fila y columna
        self.row = row
        self.col = column

    #Getters y setters
    def color (self):
        return self.color
    def color (self,n_color):
        self.color = n_color
    def image (self):
        return self.image
    def image (self,n_image):
        self.image = n_image
    def rect (self):
        return self.rect
    def rect (self,n_rect):
        self.rect = n_rect
    def row (self):
        return self.row
    def row (self,n_row):
        self.row = n_row
    def col (self):
        return self.col
    def col (self,n_col):
        self.col = n_col
