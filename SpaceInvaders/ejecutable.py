from pygame import *
import sys
from os.path import abspath, dirname
from random import choice

class GenericData ():
    """Clase con la información necesaria para el juego"""
    #Necesary routes
    DIRECT_PATH = abspath(dirname(__file__))
    IMG_PATH = DIRECT_PATH + '/Images/'
    BG_PATH = DIRECT_PATH + '/Background/'

    #Colors
    BLUE = (39, 64, 139)
    BLACK = (0,0,0)
    RED = (238, 44, 44)
    WHITE = (255, 255, 255)
    GREEN = (34, 139, 34)
    YELLOW = (255, 215, 0)

    #Screen setting
    AREA = (800,600)

    #Sprites
    IMG_KEYS = [] #Falta un diccionario que asigne al nombre de la imagen  el path necesario

    #Positions
    WALL_POS = 0
    ALIEN_START = 0
    ALIEN_MOVEX = 0
    ALIEN_MOVEY = 0

class Bullet (sprite.Sprite):
    """Clase que define el comportamiento de una bala"""
    
    def __init__(self,position_x,position_y,dirc,speed):
        super().__init__()#Iniciando la clase sprite
        self.image = image.load(GenericData.IMG_PATH +"laser.png") #extraenos la imagen para el sprite
        self.rect = self.image.get_rect() #This rectangle represent the dimensions of the sprite
        self.dirc = dirc
        self.speed = speed
        self.rect.centerx = position_x
        self.rect.centery = position_y
    def update (self):
        """Método que controla el movimiento de la bala"""
        self.rect.y -= 5
        if self.rect.y < 2 or self.rect.y > 585:
            self.kill()

class Ship (sprite.Sprite):
    """Clase que define el comportamiento de la nave"""
    def __init__(self):
        super().__init__() #Iniciando la clase sprite
        self.image = image.load(GenericData.IMG_PATH +"player.png") #extraenos la imagen para el sprite
        self.rect = self.image.get_rect() #This rectangle represent the dimensions of the sprite
        self.rect.centerx = 400
        self.rect.centery = 565
        self.speed = 20

    def update (self):
        """Método que controla el movimiento de la nave"""
        teclado=key.get_pressed()#guarda la tecla que se ha pulsado

        if teclado[K_RIGHT]:
            if self.rect.centerx < 760:
                self.rect.centerx += self.speed
        if teclado[K_LEFT]:
            if self.rect.centerx > 40 :
                self.rect.centerx -= self.speed

class Alien (sprite.Sprite):
    """Clase que define el comportamiento de un alien"""
    def __init__(self,row,col):
        super().__init__() #Iniciando la clase sprite
        self.image = image.load(GenericData.IMG_PATH +"alien.png") #extraenos la imagen para el sprite
        self.row = row
        self.col = col
        self.rect = self.image.get_rect() #This rectangle represent the dimensions of the sprite
        self.rect.centerx = 400
        self.rect.centery = 100
        self.speed = 20
    def update(self):
        pass

class AlienGroup (sprite.Group):
    """Clase que define el comportamiento del grupo de oponentes"""
    
    def __init__(self,row,col):
        sprite.Group.__init__(self)
        self.dirc = 1
        self.right = 30
        self.left = 30
        self.aliens = [[]]
        for r in range(row):
            for c in range(col):
                alien= Alien(r, c)
                alien.rect.x = 157 + (c * 50)
                alien.rect.y = 65 + (r * 45)
                self.aliens.append(alien)

    def update (self):
        pass



class SpaceInvaders (GenericData):
    """Clase que se encarga de lanzar el juego"""

    def __init__(self):
        
        #Configura el título de la ventana
        display.set_caption("Space invaders")
        #Configura el area de la pantalla
        self.screen = display.set_mode((GenericData.AREA))
        #Preparamos la imagen del background
        self.background = image.load(GenericData.BG_PATH + 'background.jpg').convert_alpha()
        #Iniciamos el reloj
        self.clock=time.Clock()
        #Inicamos la nave
        self.player = Ship()
        #Creamos un grupo de sprites
        self.spr_list = sprite.Group()
        #Creamos un grupo de balas
        self.bullets_list = sprite.Group() 
        self.spr_list.add(self.player)
        #self.enemies = AlienGroup(6,6)
        #self.spr_list.add(self.enemies.aliens)
    def redraw(self):
        #Pegamos los sprites
        self.screen.blit(self.background, (0, 0))#ponemos el background
        self.screen.blit(self.player.image,self.player.rect)# añadimos la nave

        #for r in range(6):
        #   for c in range(6):
        #      self.screen.blit(self.enemies.aliens[r][c].image,self.enemies.aliens[r][c].rect)

        #Recorremos la lista de balas actualizandolas
        for i in self.bullets_list:
            self.screen.blit(i.image, i.rect)
        #Actualizamos pantalla
        display.update()

    def ship_shoot(self):
        """Método para que la nave dispare"""
        
        #Recogemos los eventos
        events = event.get()
        
        #Controlamos el boton espacio para disparar
        for even in events:
            if even.type == KEYDOWN:
                if even.key == K_SPACE:
    
                    #Creamos la bala
                    bullet = Bullet(self.player.rect.centerx,self.player.rect.top-10,-1,1)
                    
                    #Añadimos la bala a la lista de balas
                    self.bullets_list.add(bullet)

                    #Añadimos la bala a la lista de sprites
                    self.spr_list.add(bullet)
                        
                    #Pegamos la bala a la pantalla    
                    self.screen.blit(bullet.image, bullet.rect)




    def main (self):
        
        #Pygame init
        init()
        
        #Iniciamos la clase
        self.__init__()

        #Bucle principal
        while True:

            #Fps
            self.clock.tick(30)

            #Pegamos el background
            self.screen.blit(self.background, (0, 0))
            
            #Pegamos la nave
            self.screen.blit(self.player.image,self.player.rect)
            
            #self.screen.blit(self.alien.image,self.alien.rect)
            #for r in range(6):
            #    for c in range(6):
            #        self.screen.blit(self.enemies.aliens[r][c].image,self.enemies.aliens[r][c].rect)

            #Método para disparar
            self.ship_shoot()
            
            #Actualizamos todos los sprites
            self.spr_list.update()
            
            #Método para redibujar la pantalla y que funcione el movimiento
            self.redraw()

            #El usuario hizo algo
            for evento in event.get(): 
                if evento.type == QUIT:
                    sys.exit()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
