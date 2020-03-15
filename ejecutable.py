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


class Ship (sprite.Sprite):
    def __init__(self):
        super().__init__() #Iniciando la clase sprite
        self.image = image.load(GenericData.IMG_PATH +"player2.png").convert() #extraenos la imagen para el sprite
        self.rect = self.image.get_rect() #This rectangle represent the dimensions of the sprite
        self.rect.centerx = 400
        self.rect.centery = 550
        self.speed = 8
    def update (self):
        pass
       


class SpaceInvaders (GenericData):

    def __init__(self):
        display.set_caption("Space invaders") #Configura el titulo de la ventana
        self.screen = display.set_mode((GenericData.AREA)) #Configura el area de la pantalla
        self.background = image.load(GenericData.BG_PATH + 'background.jpg').convert_alpha()#preparamos la imagen del background
        self.clock=time.Clock() #iniciamos el reloj
        self.player = Ship() #inicamos la nave
        

        
    def main (self):

        self.__init__()
        init() #pygame init
        self.screen.blit(self.background, (0, 0))#ponemos el background
        self.screen.blit(self.player.image,self.player.rect)# añadimos la nave

        while True:
            teclado=key.get_pressed()
            if teclado[K_RIGHT]:
                self.player.rect.centerx += 8
        
 
            if teclado[K_LEFT]:
                self.player.rect.centerx -= 8
                
            self.screen.blit(self.player.image,self.player.rect)# añadimos la nave
            display.flip()#actualizamos la screen
            
            for evento in event.get(): # El usuario hizo algo
                if evento.type == QUIT:
                    sys.exit()
            
            
            self.clock.tick(60)#fps
            
        



if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
