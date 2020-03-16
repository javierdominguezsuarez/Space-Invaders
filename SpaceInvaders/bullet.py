from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata

class Bullet (sprite.Sprite):
    """Clase que define el comportamiento de una bala"""

    def __init__(self,position_x,position_y,dirc,speed):
        #Iniciando la clase sprite
        super().__init__()
        #Extraenos la imagen para el sprite
        self.image = image.load(GenericData.IMG_PATH +"laser.png")
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        self.dirc = dirc
        self.speed = speed
        self.rect.centerx = position_x
        self.rect.centery = position_y
    def update (self):
        """Método que controla el movimiento de la bala"""
        self.rect.y -= 5
        if self.rect.y < 2 or self.rect.y > 585:
            self.kill()
