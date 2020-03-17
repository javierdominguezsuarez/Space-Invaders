from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import genericdata, bullet , ship, alien, aliengroup, text, life, wall

class SpaceInvaders (GenericData,sprite.Sprite):
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
        #Creamos un grupo de aliens
        self.aliens_list = sprite.Group()

        #Grupo nave
        self.player_list = sprite.Group()
        self.player_list.add(self.player)
        self.spr_list.add(self.player)
        #Reloj
        self.timer = time.get_ticks()
        
        #Disparos alien
        self.ab_bullets = sprite.Group()
        self.spr_list_ab = sprite.Group()

        self.life_counter = 3
        self.score_counter = 0
        
        for enemy in range(20):
            
                alien= Alien()
                alien.rect.x = random.randint(5,800)
                alien.rect.y = random.randint(5,320)
                
                self.aliens_list.add(alien)
                self.spr_list.add(alien)
                self.screen.blit(alien.image,alien.rect)
                
        
    def text (self,vidas):
        """Método para mostrar la puntuación"""
        
        #Iniciando la clase sprite
        super().__init__()

        self.font_used = font.Font(None, 59)
        self.number_score = self.font_used.render(str(self.score_counter), 0, (255, 255, 255))
        
        self.image_lives = image.load(GenericData.BG_PATH +"lives.png")
        self.rect_lives = self.image_lives.get_rect()
        self.rect_lives.centerx =  610
        self.rect_lives.centery = 20

        self.image_score = image.load(GenericData.BG_PATH +"score.png")
        self.rect_score = self.image_score.get_rect()
        self.rect_score.centerx =  60
        self.rect_score.centery = 20
        
        self.image_heart_one = image.load(GenericData.BG_PATH +"heart.png")
        self.rect_heart_one = self.image_heart_one.get_rect()
        self.rect_heart_one.centerx = 690
        self.rect_heart_one.centery = 19
        #self.spr_list.add(self.image_heart_one)
        
        self.image_heart_two = image.load(GenericData.BG_PATH +"heart.png")
        self.rect_heart_two = self.image_heart_two.get_rect()
        self.rect_heart_two.centerx = 730
        self.rect_heart_two.centery = 19
        #self.spr_list.add(self.image_heart_two)
        
        self.image_heart_three = image.load(GenericData.BG_PATH +"heart.png")
        self.rect_heart_three = self.image_heart_three.get_rect()
        self.rect_heart_three.centerx = 770
        self.rect_heart_three.centery = 19
        #self.spr_list.add(self.image_heart_three)
        
        self.screen.blit(self.image_lives,self.rect_lives)
        self.screen.blit(self.image_score,self.rect_score)
        self.screen.blit(self.number_score,(130,4))
        if vidas > 0:
            
            self.screen.blit(self.image_heart_one,self.rect_heart_one)
            
        if vidas > 1 :
            
            self.screen.blit(self.image_heart_two,self.rect_heart_two)
            
        if vidas == 3  :
            
            self.screen.blit(self.image_heart_three,self.rect_heart_three)

            
    def redraw(self):
        #Pegamos los sprites
        self.screen.blit(self.background, (0, 0))#ponemos el background
        self.screen.blit(self.player.image,self.player.rect)# añadimos la nave
        
        self.screen.blit(self.image_lives,self.rect_lives)
        self.screen.blit(self.image_score,self.rect_score)
        self.screen.blit(self.number_score,(130,4))
                         
        if self.life_counter > 0:
            
            self.screen.blit(self.image_heart_one,self.rect_heart_one)
            
        if self.life_counter > 1:
            
            self.screen.blit(self.image_heart_two,self.rect_heart_two)
            
        if self.life_counter == 3 :
            
            self.screen.blit(self.image_heart_three,self.rect_heart_three)
        
        for j in self.aliens_list:
            self.screen.blit(j.image, j.rect)
        #Recorremos la lista de balas actualizandolas
        for i in self.bullets_list:
            self.screen.blit(i.image, i.rect)
        for k in self.ab_bullets:
            self.screen.blit(k.image, k.rect)
       
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
                    bullet = Bullet(self.player.rect.centerx,self.player.rect.top-10,-1,12,1)

                    #Añadimos la bala a la lista de balas
                    self.bullets_list.add(bullet)

                    #Añadimos la bala a la lista de sprites
                    self.spr_list.add(bullet)

                    #Pegamos la bala a la pantalla
                    self.screen.blit(bullet.image, bullet.rect)

    def alien_shoot(self):
        """Método para que la nave dispare"""
        #hay protecciones, lo que no la hemos hecho
        #Creamos la bala
        if (time.get_ticks() - self.timer) > 700:
            self.a_list = self.aliens_list.sprites()
            tam = len(self.a_list)
            if tam != 0:
                alien = self.a_list[randrange(tam)]
                bullet = Bullet(alien.rect.centerx,alien.rect.bottom +5,1,10,0)

                #Añadimos la bala a la lista de balas
                self.ab_bullets.add(bullet)

                #Añadimos la bala a la lista de sprites
                self.spr_list_ab.add(bullet)

                #Pegamos la bala a la pantalla
                self.screen.blit(bullet.image, bullet.rect)

                self.timer = time.get_ticks()

        
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

            

            #Método para disparar
            self.ship_shoot()
            
            #Método de disparo de los alien
            self.alien_shoot()
            
            #Actualizamos todos los sprites
            self.spr_list.update()
            self.spr_list_ab.update()

            #Colisiones Alien
            for bullet in self.bullets_list:
                alien_shot = sprite.spritecollide(bullet, self.aliens_list, True)

                for alien in alien_shot:
                    self.score_counter+=50
                    self.bullets_list.remove(bullet)
                    self.spr_list.remove(bullet)
            #Colisiones Nave
            for bullet in self.ab_bullets:
                if self.life_counter > 1:
                    
                    player_shot = sprite.spritecollide(bullet, self.player_list,False)
                    for player in player_shot:
                        self.life_counter-=1
                        self.ab_bullets.remove(bullet)
                        self.spr_list_ab.remove(bullet)
                else  :
                    
                    player_shot = sprite.spritecollide(bullet, self.player_list,False)
                    for player in player_shot:
                        self.life_counter=3
                        self.score_counter= 0
                        self.ab_bullets.remove(bullet)
                        self.spr_list_ab.remove(bullet)
                        
            self.text(self.life_counter)
            #Método para redibujar la pantalla y que funcione el movimiento
            self.redraw()
            
            #El usuario hizo algo 
            for evento in event.get():
                if evento.type == QUIT:
                    sys.exit()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
