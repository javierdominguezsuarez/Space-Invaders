from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata
import alien

class AlienGroup (sprite.Group):
    """Clase que define el comportamiento del grupo de oponentes"""

    def __init__(self,row,col):
        sprite.Group.__init__(self)
        self.dirc = 1
        self.right = 30
        self.left = 30
        self.aliens = [[]]
        for r in range(row):
            for c in range(col):
                alien= Alien(r, c)
                alien.rect.x = 157 + (c * 50)
                alien.rect.y = 65 + (r * 45)
                self.aliens.append(alien)

    def update (self):
        pass
