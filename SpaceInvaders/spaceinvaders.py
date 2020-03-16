from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata, bullet , ship, alien, aliengroup, text, life, wall

class SpaceInvaders (GenericData):
    """Clase que se encarga de lanzar el juego"""

    def __init__(self):

        #Configura el título de la ventana
        display.set_caption("Space invaders")
        #Configura el area de la pantalla
        self.screen = display.set_mode((GenericData.AREA))
        #Preparamos la imagen del background
        self.background = image.load(GenericData.BG_PATH + 'background.jpg').convert_alpha()
        #Iniciamos el reloj
        self.clock=time.Clock()
        #Inicamos la nave
        self.player = Ship()
        #Creamos un grupo de sprites
        self.spr_list = sprite.Group()
        #Creamos un grupo de balas
        self.bullets_list = sprite.Group()
        self.spr_list.add(self.player)
        #self.enemies = AlienGroup(6,6)
        #self.spr_list.add(self.enemies.aliens)

    def redraw(self):
        #Pegamos los sprites
        self.screen.blit(self.background, (0, 0))#ponemos el background
        self.screen.blit(self.player.image,self.player.rect)# añadimos la nave

        #for r in range(6):
        #   for c in range(6):
        #      self.screen.blit(self.enemies.aliens[r][c].image,self.enemies.aliens[r][c].rect)

        #Recorremos la lista de balas actualizandolas
        for i in self.bullets_list:
            self.screen.blit(i.image, i.rect)
        #Actualizamos pantalla
        display.update()

    def ship_shoot(self):
        """Método para que la nave dispare"""

        #Recogemos los eventos
        events = event.get()

        #Controlamos el boton espacio para disparar
        for even in events:
            if even.type == KEYDOWN:
                if even.key == K_SPACE:

                    #Creamos la bala
                    bullet = Bullet(self.player.rect.centerx,self.player.rect.top-10,-1,1)

                    #Añadimos la bala a la lista de balas
                    self.bullets_list.add(bullet)

                    #Añadimos la bala a la lista de sprites
                    self.spr_list.add(bullet)

                    #Pegamos la bala a la pantalla
                    self.screen.blit(bullet.image, bullet.rect)




    def main (self):

        #Pygame init
        init()

        #Iniciamos la clase
        self.__init__()

        #Bucle principal
        while True:

            #Fps
            self.clock.tick(30)

            #Pegamos el background
            self.screen.blit(self.background, (0, 0))

            #Pegamos la nave
            self.screen.blit(self.player.image,self.player.rect)

            #self.screen.blit(self.alien.image,self.alien.rect)
            #for r in range(6):
            #    for c in range(6):
            #        self.screen.blit(self.enemies.aliens[r][c].image,self.enemies.aliens[r][c].rect)

            #Método para disparar
            self.ship_shoot()

            #Actualizamos todos los sprites
            self.spr_list.update()

            #Método para redibujar la pantalla y que funcione el movimiento
            self.redraw()

            #El usuario hizo algo
            for evento in event.get():
                if evento.type == QUIT:
                    sys.exit()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
