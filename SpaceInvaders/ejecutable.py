from pygame import *
import sys
from os.path import abspath, dirname
from random import choice

class GenericData ():
    """Class with the necesary data for the main class"""
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
    def __init__(self,position_x,position_y,dirc,speed):
        super().__init__()#Iniciando la clase sprite
        self.image = image.load(GenericData.IMG_PATH +"laser.png") #extraenos la imagen para el sprite
        self.rect = self.image.get_rect() #This rectangle represent the dimensions of the sprite
        self.dirc = dirc
        self.speed = speed
        self.rect.centerx = position_x
        self.rect.centery = position_y
    def update (self):
        self.rect.y -= 1
        #if self.rect.y < 15 or self.rect.y > 585:
         #   self.kill()
    
class Ship (sprite.Sprite):
    def __init__(self):
        super().__init__() #Iniciando la clase sprite
        self.image = image.load(GenericData.IMG_PATH +"player4.png") #extraenos la imagen para el sprite
        self.rect = self.image.get_rect() #This rectangle represent the dimensions of the sprite
        self.rect.centerx = 400
        self.rect.centery = 565
        self.speed = 28
        
    def update (self):
        
        """método que controla el movimiento de la nave"""
        teclado=key.get_pressed()#guarda la tecla que se ha pulsado

        if teclado[K_RIGHT]:
            if self.rect.centerx < 775:
                self.rect.centerx += self.speed
        if teclado[K_LEFT]:
            if self.rect.centerx > 25 :
                self.rect.centerx -= self.speed


class SpaceInvaders (GenericData):

    def __init__(self):
        display.set_caption("Space invaders") #Configura el titulo de la ventana
        self.screen = display.set_mode((GenericData.AREA)) #Configura el area de la pantalla
        self.background = image.load(GenericData.BG_PATH + 'background.jpg').convert_alpha()#preparamos la imagen del background
        self.clock=time.Clock() #iniciamos el reloj
        self.player = Ship() #inicamos la nave
        
    def redraw(self):
        self.screen.blit(self.background, (0, 0))#ponemos el background
        self.screen.blit(self.player.image,self.player.rect)# añadimos la nave
        display.update()
        
    def ship_shoot(self):
        #self.screen.blit(self.image, self.rect)
        
        bullet = Bullet(self.player.rect.centerx,self.player.rect.top-10,-1,1)#creamos la bala
        
        while bullet.rect.top > 5:
            bullet.update()
            self.screen.blit(self.background, (0, 0))#ponemos el background
            self.screen.blit(bullet.image, bullet.rect)
            self.screen.blit(self.player.image,self.player.rect)# añadimos la nave
            display.update()
            
            
            
            
        
        
        
    def main (self):

        self.__init__()
        init() #pygame init
        

        while True:
            
            self.clock.tick(30)#fps
            

            self.screen.blit(self.background, (0, 0))#ponemos el background
            self.screen.blit(self.player.image,self.player.rect)# añadimos la nave
            self.player.update()#movimiento de la nave
            
            
            
            self.ship_shoot()
            self.redraw()#método para redibujar la pantalla y que funcione el movimiento
            
            for evento in event.get(): # El usuario hizo algo
                if evento.type == QUIT:
                    sys.exit()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
