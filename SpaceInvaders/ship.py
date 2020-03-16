from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata


class Ship (sprite.Sprite):
    """Clase que define el comportamiento de la nave"""
    def __init__(self):
        #Iniciando la clase sprite
        super().__init__()
        #Extraenos la imagen para el sprite
        self.image = image.load(GenericData.IMG_PATH +"player.png")
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 565
        self.speed = 20

    def update (self):
        """Método que controla el movimiento de la nave"""
        #Guarda la tecla que se ha pulsado
        teclado=key.get_pressed()

        if teclado[K_RIGHT]:
            if self.rect.centerx < 760:
                self.rect.centerx += self.speed
        if teclado[K_LEFT]:
            if self.rect.centerx > 40 :
                self.rect.centerx -= self.speed
