from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata


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
