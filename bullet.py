from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata

class Bullet (sprite.Sprite):
    """Clase que define el comportamiento de una bala"""
    
    def __init__(self,coord_x,coord_y,dirc,speed,ship_shot):
        """Método para iniciar el objeto"""
        #Iniciando la clase sprite
        super().__init__()

        try :
            #Extraenos la imagen para el sprite
            if ship_shot == 1 :
                self.image = image.load(GenericData.IMG_PATH +"laser.png")
            else :
                self.image = image.load(GenericData.AL_PATH +"laser_a.png")
        except FileNotFoundError :
            print("Sprite de la bala no encontrado")
        
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        #Asignamos dirección y velocidad
        self.dirc = dirc
        self.speed = speed
        
        assert type(coord_x) == int  and type(coord_y) == int ,"Error de tipo en coordenadas"
        assert type(dirc) == int  and type(speed) == int ,"Error de tipo en parámetros de la bala"
        
        #Asignamos su posición de salida
        self.rect.centerx = coord_x
        self.rect.centery = coord_y
        
    def update (self):
        """Método que controla el movimiento de la bala"""
        #Variamos su posición para moverla
        self.rect.y += self.speed * self.dirc
        #Si llega a la parte inferior la eliminamos 
        if self.rect.y < 2 or self.rect.y > 585:
            self.kill() 
    #Getters y setters
    def dirc (self):
        return self.dirc
    def dirc (self,n_dirc):
        self.dirc = n_dirc
    def image (self):
        return self.image
    def image (self,n_image):
        self.image = n_image
    def rect (self):
        return self.rect
    def rect (self,n_rect):
        self.rect = n_rect
    def speed (self):
        return self.speed
    def speed (self,n_speed):
        self.speed = n_speed
    
        
