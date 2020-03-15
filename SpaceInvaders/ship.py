from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata


class Ship (sprite.Sprite):
    def __init__(self):
        super().__init__() #Iniciando la clase sprite
        self.image = image.load(GenericData.IMG_PATH +"player4.png") #extraenos la imagen para el sprite
        self.rect = self.image.get_rect() #This rectangle represent the dimensions of the sprite
        self.rect.centerx = 400
        self.rect.centery = 565
        self.speed = 20

    def update (self):
        """método que controla el movimiento de la nave"""
        teclado=key.get_pressed()#guarda la tecla que se ha pulsado

        if teclado[K_RIGHT]:
            if self.rect.centerx < 775:
                self.rect.centerx += self.speed
        if teclado[K_LEFT]:
            if self.rect.centerx > 25 :
                self.rect.centerx -= self.speed
