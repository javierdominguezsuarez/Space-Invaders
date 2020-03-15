from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata, bullet , ship, alien, aliengroup, text, life, wall

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
