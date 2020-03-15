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
    AREA = (800,800)

    #Sprites
    IMG_KEYS = [] #Falta un diccionario que asigne al nombre de la imagen  el path necesario

    #Positions
    WALL_POS = 0
    ALIEN_START = 0
    ALIEN_MOVEX = 0
    ALIEN_MOVEY = 0
    #Inmutable
    def __setattr__(self):
        raise AttributeError("Can't set attribute")
