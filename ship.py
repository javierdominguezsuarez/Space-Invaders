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

        try:
            #Extraenos la imagen para el sprite
            self.image = image.load(GenericData.IMG_PATH +"player.png")
        except FileNotFoundError :
            print("Sprite de la nave no encontrado")
        
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 565
        #Establecemos la velocidad del movimiento de la nave
        self.speed = 15
        
        #AÑADIR GETTER Y SETTER (ATRIBUTOS CHANGE X , CHANGE Y)
        #Atributos para guardar las coordenadas de la animación
        self.changex = 0
        self.changey = 0
        
        
    def update (self):
        """Método que controla el movimiento de la nave"""

        #Guardamos las cordenadas actuales de la nave
        self.changex = self.rect.centerx
        self.changey = self.rect.centery

        #Esto sirve para que cuando no se mueva la nave el fuego vuelva al centro
        try:
            #Extraenos la imagen para el sprite
            self.image = image.load(GenericData.IMG_PATH +"player.png")
        except FileNotFoundError :
            print("Sprite de la nave no encontrado")
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()

        #Igualamos a las coordenadas guardadas
        self.rect.centerx = self.changex
        self.rect.centery = self.changey

        #Guarda la tecla que se ha pulsado
        teclado=key.get_pressed()

        #Acciones que ocurren cuando la nave se mueve a la derecha (se apreta la tecla K_RIGHT)
        if teclado[K_RIGHT]:
            if self.rect.centerx < 760:
                
                try:
                    #Extraenos la imagen para el sprite
                    self.image = image.load(GenericData.IMG_PATH +"player_r.png")
                except FileNotFoundError :
                    print("Sprite de la nave no encontrado")
                #Esta función nos devuelve un objeto con las dimensiones del sprite
                self.rect = self.image.get_rect()
                #Copiamos las coordenadas guardadas
                self.rect.centerx = self.changex
                self.rect.centery = self.changey
                #Movemos el sprite
                self.rect.centerx += self.speed
                

        #Acciones que ocurren cuando la nave se mueve a la izquierda (se apreta la tecla K_LEFT)           
        if teclado[K_LEFT]:
            if self.rect.centerx > 40 :
                
                try:
                    #Extraenos la imagen para el sprite
                    self.image = image.load(GenericData.IMG_PATH +"player_l.png")
                except FileNotFoundError :
                    print("Sprite de la nave no encontrado")
                #Esta función nos devuelve un objeto con las dimensiones del sprite
                self.rect = self.image.get_rect()
                #Copiamos las coordenadas guardadas
                self.rect.centerx = self.changex
                self.rect.centery = self.changey
                #Movemos el sprite
                self.rect.centerx -= self.speed
                
                
    #Getters y setters
    def changex (self):
        return self.changex
    def changex (self,n_changex):
        self.changex = n_changex
    def changey (self):
        return self.changey
    def changey (self,n_changey):
        self.changey = n_changey
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
    
                
    def burn (self):
        """Método que devuelve las coordenadas de la nave para poder realizar la animación de explosión"""
        #Atributos para guardar las coordenadas en la animación
        return (self.rect.centerx,self.rect.centery)
    

