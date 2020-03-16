from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata

class Alien (sprite.Sprite):
    """Clase que define el comportamiento de un alien"""
    def __init__(self,row,col):
        #Iniciando la clase sprite
        super().__init__()
        #Extraenos la imagen para el sprite
        self.image = image.load(GenericData.IMG_PATH +"alien.png")
        self.row = row
        self.col = col
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 100
        self.speed = 20
    def update(self):
        pass
