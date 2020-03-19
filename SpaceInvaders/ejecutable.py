from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
import random
from random import randrange

class GenericData ():
    """Clase con la información necesaria para el juego"""
    #Necesary routes
    DIRECT_PATH = abspath(dirname(__file__))
    IMG_PATH = DIRECT_PATH + '/Ship/'
    BG_PATH = DIRECT_PATH + '/Background/'
    AL_PATH = DIRECT_PATH + '/Alien/'
    #Colors
    BLUE = (39, 64, 139)
    BLACK = (0,0,0)
    RED = (238, 44, 44)
    WHITE = (255, 255, 255)
    PURPLE = (164,3,155)
    PINK = (255,6,191)
    #Screen setting
    AREA = (800,600)

class Wall (sprite.Sprite):
    """Clase que define el comportamiento de un muro"""
    
    def __init__(self,x,y,r,c,b):
        
        super().__init__()
        
        
        self.color = b  
        self.image = Surface((10,10))
        if self.color == 0 :
            self.image.fill((164,3,155))
        else :
            self.image.fill((255,6,191))
            
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.row = r
        self.col = c

        
    
class Bullet (sprite.Sprite):
    """Clase que define el comportamiento de una bala"""
    
    def __init__(self,position_x,position_y,dirc,vec,sa):
        #Iniciando la clase sprite
        super().__init__()
        #Extraenos la imagen para el sprite
        if sa == 1 :
            self.image = image.load(GenericData.IMG_PATH +"laser.png")
        else :
            self.image = image.load(GenericData.AL_PATH +"laser_a.png")
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        self.dirc = dirc
        self.vec = vec
        self.rect.centerx = position_x
        self.rect.centery = position_y
    def update (self):
        """Método que controla el movimiento de la bala"""
        self.rect.y += self.vec * self.dirc
        if self.rect.y < 2 or self.rect.y > 585:
            self.kill() 

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
        self.speed = 15
        #Atributos para guardar las coordenadas en la animaciónn
        self.changex = 0
        self.changey = 0
        
        
    def update (self):
        """Método que controla el movimiento de la nave"""

        #Guardamos las cordenadas actuales para no perderlas
        self.changex = self.rect.centerx
        self.changey = self.rect.centery

        #Esto sirve para que cuando no se mueva la nave el fuego vuelva al centro
        #Extraenos la imagen para el sprite
        self.image = image.load(GenericData.IMG_PATH +"player.png")
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()

        #Igualamos a alas coordenadas guardadas
        self.rect.centerx = self.changex
        self.rect.centery = self.changey

        #Guarda la tecla que se ha pulsado
        teclado=key.get_pressed()
        
        if teclado[K_RIGHT]:
            if self.rect.centerx < 760:
                
                #Extraenos la imagen para el movimiento a la derecha
                self.image = image.load(GenericData.IMG_PATH +"player_r.png")
                #Esta función nos devuelve un objeto con las dimensiones del sprite
                self.rect = self.image.get_rect()
                #Copiamos las coordenadas guardadas
                self.rect.centerx = self.changex
                self.rect.centery = self.changey
                #Movemos el sprite
                self.rect.centerx += self.speed
                
                       
        if teclado[K_LEFT]:
            if self.rect.centerx > 40 :
                
                #Extraenos la imagen para el movimiento a la izquierda
                self.image = image.load(GenericData.IMG_PATH +"player_l.png")
                #Esta función nos devuelve un objeto con las dimensiones del sprite
                self.rect = self.image.get_rect()
                #Copiamos las coordenadas guardadas
                self.rect.centerx = self.changex
                self.rect.centery = self.changey
                #Movemos el sprite
                self.rect.centerx -= self.speed
                
                
                
    def burn (self):
        
        #Atributos para guardar las coordenadas en la animación
        return (self.rect.centerx,self.rect.centery)
    
class Alien (sprite.Sprite):
    """Clase que define el comportamiento de un alien"""
    def __init__(self,speed):
        #Iniciando la clase sprite
        super().__init__()
        #Extraenos la imagen para el sprite
        self.image = image.load(GenericData.AL_PATH +"alien.png")
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        self.dir = 1
        self.speed = speed

        #Atributos para guardar las coordenadas en la animación
        self.changex = 0
        self.changey = 0
        
    def update(self):
        
        if self.rect.x < 750 :
            self.rect.x+= self.speed * self.dir
        elif self.rect.x > 750:
            self.dir=-1
            self.rect.y +=13
        if self.rect.x > 3:
            self.rect.x+= self.speed * self.dir
        elif self.rect.x < 3:
            self.rect.y +=13
            self.dir=1
            
        if self.rect.y >=590:
            self.kill()
        
    def burn (self):
        
        #Atributos para guardar las coordenadas en la animación
        return (self.rect.centerx,self.rect.centery)
        
class Explotion (sprite.Sprite):

    def __init__(self,pos,tipe):

        super().__init__()
        if tipe == 0 :
            #Extraenos la imagen para la explosión
            self.image = image.load(GenericData.AL_PATH +"explosion.png")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
        elif tipe == 1 :
            #Extraenos la imagen para la explosión
            self.image = image.load(GenericData.IMG_PATH +"explosion_ship1.png")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
            
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.clk = time.get_ticks()
        
        
        
    def update(self):
        if (time.get_ticks() - self.clk) > 70 :
            self.kill()
        
        
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
        self.init_sound()
        #Grupo nave
        self.player_list = sprite.Group()
        self.player_list.add(self.player)
        self.spr_list.add(self.player)
        
        #Reloj
        self.timer = time.get_ticks()
        
        #Disparos alien
        self.ab_bullets = sprite.Group()
        self.spr_list_ab = sprite.Group()

        #Contador de visas
        self.life_counter = 3
        #Contador de score
        self.score_counter = 0
        #Numero de aliens de la ronda
        self.ronda = 5
        #Incremento de ovnis
        self.incremento = 3
        #Tiempo de disparo
        self.shot_time = 550
        #Incremento de velocidad de ovnis
        self.speed_ronda = 2
        
        #Creamos los aliens
        self.create_aliens(self.ronda,self.speed_ronda)

        #Grupo muros
        self.wall_group = sprite.Group()
        self.init_wall()

        #Grupo de explosiones
        self.exp_group = sprite.Group()
        
    def init_sound (self):
        
        #Musica
        mixer.init()
        self.main_music = mixer.music.load(GenericData.BG_PATH + 'music.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.05)
        #Sonido disparo
        self.shot_sound = mixer.Sound("shot.wav")
        #Sonido explosión alien
        self.crash_alien_sound = mixer.Sound("ca.wav")
        mixer.Sound.set_volume(self.crash_alien_sound,0.1)
        #Sonido explosion nave
        self.crash_ship_sound = mixer.Sound("cs.wav")
        mixer.Sound.set_volume(self.crash_ship_sound,0.1)
        #Sonido explosión final nave
        self.restart_sound = mixer.Sound("last.wav")
        mixer.Sound.set_volume(self.restart_sound,0.1)
        
    def init_wall(self):

        for row in range(6):
            for col in range(15):
                #print("Fila: "+str(row)+"   Col : "+str(col))
                #Primer bloque
                x = 50 + (25) + (col * 10)
                y = 435 +  (row * 10)
                #Segundo bloque
                t= 50 + (276) + (col * 10)
                s= 435 +  (row * 10)
                #Tercer bloque
                r = 50 + (530) + (col * 10)
                w = 435 +  (row * 10)
                
                if row == 0 or row == 5 :
                    
                    wall = Wall(x,y,row,col,0)
                    wall_sec = Wall(t,s,row,col,0)
                    wall_third = Wall(r,w,row,col,0)
                    
                    
                else :
                    
                    wall = Wall(x,y,row,col,1)
                    wall_sec = Wall(t,s,row,col,1)
                    wall_third = Wall(r,w,row,col,1)
                    
                   
                self.wall_group.add(wall)
                self.screen.blit(wall.image, wall.rect)
                
                self.wall_group.add(wall_sec)
                self.screen.blit(wall_sec.image, wall_sec.rect)
                    
                self.wall_group.add(wall_third)
                self.screen.blit(wall_third.image,wall_third.rect)
                
               
                    
                


    def create_aliens (self,n,s):
        for enemy in range(n):
            
                alien= Alien(s)
                alien.rect.x = random.randint(5,800)
                alien.rect.y = random.randint(5,300)
                
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
        
        
        self.image_heart_two = image.load(GenericData.BG_PATH +"heart.png")
        self.rect_heart_two = self.image_heart_two.get_rect()
        self.rect_heart_two.centerx = 730
        self.rect_heart_two.centery = 19
        
        
        self.image_heart_three = image.load(GenericData.BG_PATH +"heart.png")
        self.rect_heart_three = self.image_heart_three.get_rect()
        self.rect_heart_three.centerx = 770
        self.rect_heart_three.centery = 19
        
        
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
        
        
        #Recorremos la lista de balas actualizandolas
        for j in self.aliens_list:
            self.screen.blit(j.image, j.rect)
            
        for i in self.bullets_list:
            self.screen.blit(i.image, i.rect)
            
        for k in self.ab_bullets:
            self.screen.blit(k.image, k.rect)

        for l in self.wall_group:
            self.screen.blit(l.image, l.rect)

        for m in self.exp_group:
            m.update()
            self.screen.blit(m.image,m.rect)
        
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

                    #Activamos sonido de disparo
                    mixer.Sound.play(self.shot_sound)
                    
                    #Creamos la bala
                    bullet = Bullet(self.player.rect.centerx,self.player.rect.top,-1,22,1)

                    
                    
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
        if self.shot_time > 200 and self.ronda >15:
            self.shot_time -=50
            
        if (time.get_ticks() - self.timer) > self.shot_time:
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

    def colitions (self):
            #Colisiones Alien
            for bullet in self.bullets_list:
                alien_shot = sprite.spritecollide(bullet, self.aliens_list, True)
                
                for alien in alien_shot:
                    exp = Explotion(alien.burn(),0)
                    self.exp_group.add(exp)
                    mixer.Sound.play(self.crash_alien_sound)
                    self.score_counter+=50
                    self.bullets_list.remove(bullet)
                    self.spr_list.remove(bullet)
                    

                    
                self.a_list = self.aliens_list.sprites()
                tam = len(self.a_list)
                if tam == 0:
                    if self.ronda < 24:
                        self.ronda += self.incremento
                    if self.speed_ronda <11 and self.ronda > 13:
                        self.speed_ronda +=1
                    self.create_aliens(self.ronda,self.speed_ronda)
                    #Colocamos los muros de nuevo
                    self.init_wall()
                        
            #Colisiones balas con balas
            sprite.groupcollide(self.bullets_list, self.ab_bullets, True, True)
            
            #Colisiones  muros
            sprite.groupcollide(self.bullets_list, self.wall_group, True, True)
            sprite.groupcollide(self.ab_bullets, self.wall_group, True, True)
            
            sprite.groupcollide(self.aliens_list, self.wall_group, False, True)
            
            #Colisiones Nave balas
            for bullet in self.ab_bullets:
                if self.life_counter > 1:
                    
                    player_shot = sprite.spritecollide(bullet, self.player_list,False)
                    
                    for player in player_shot:
                        #Ponemos explosion
                        exp = Explotion(player.burn(),1)
                        self.exp_group.add(exp)
                        
                        mixer.Sound.play(self.crash_ship_sound)
                        self.life_counter-=1
                        self.ab_bullets.remove(bullet)
                        self.spr_list_ab.remove(bullet)
                else  :
                    
                    player_shot = sprite.spritecollide(bullet, self.player_list,False)
                    for player in player_shot:
                        mixer.Sound.play(self.restart_sound)
                        self.life_counter=3
                        #Ponemos explosion
                        exp = Explotion(player.burn(),1)
                        self.exp_group.add(exp)
                        #Si perdemos, quitamos los aliens
                        for a in self.aliens_list:
                            self.aliens_list.remove(a)
                                
                        time.wait(750)

                        #Eliminamos las balas
                        self.ab_bullets.remove(bullet)
                        self.spr_list_ab.remove(bullet)
                        
                        #Y volvemos a empezar
                        self.shot_time = 550
                        self.ronda = 5
                        self.speed_ronda = 2
                        self.create_aliens(self.ronda,self.speed_ronda)

                        #Restablecemos score
                        self.score_counter= 0

                        
                        #Colocamos los muros de nuevo
                        self.init_wall()
                        
            #Colisiones alien-nave
            for ali in self.aliens_list:
                if self.life_counter > 1:
                    
                    player_shot = sprite.spritecollide(ali, self.player_list,False)
                    for player in player_shot:
                        #Ponemos explosion nave
                        exp = Explotion(player.burn(),1)
                        self.exp_group.add(exp)
                        #Ponemos explosion alien
                        exp = Explotion(ali.burn(),0)
                        self.exp_group.add(exp)
                        #Sonido
                        mixer.Sound.play(self.crash_ship_sound)
                        self.life_counter-=1
                        self.aliens_list.remove(ali)
                        self.spr_list.remove(ali)
                else  :
                    
                    player_shot = sprite.spritecollide(ali, self.player_list,False)
                    for player in player_shot:
                        #Ponemos explosion
                        exp = Explotion(player.burn(),1)
                        self.exp_group.add(exp)
                        #Ponemos explosion alien
                        exp = Explotion(ali.burn(),0)
                        self.exp_group.add(exp)
                        #Sonido
                        mixer.Sound.play(self.restart_sound)
                        self.life_counter=3
                        
                        #Si perdemos, quitamos los aliens
                        for a in self.aliens_list:
                            self.aliens_list.remove(a)
                            
                        time.wait(750)
                        #Y volvemos a empezar
                        self.shot_time = 550
                        self.ronda = 5
                        self.speed_ronda = 2
                        self.create_aliens(self.ronda,self.speed_ronda)

                        #Restablecemos score
                        self.score_counter= 0
                        
                        #Colocamos los muros de nuevo
                        self.init_wall()

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

            #Método de disparo de los alien
            self.alien_shoot()
            
            #Método para disparar
            self.ship_shoot()
            
            #Método de disparo de los alien
            self.alien_shoot()
            
            #Actualizamos todos los sprites
            self.spr_list.update()
            self.spr_list_ab.update()
            
           
            
            self.ship_shoot()
            #Controlamos las colisiones entre objetos
            self.colitions()
            
            
            self.ship_shoot()
            
            #Añadimos el texto a la pantalla          
            self.text(self.life_counter)
            
            
            
            #Método para redibujar la pantalla y que funcione el movimiento
            self.redraw()

            self.ship_shoot()
            
            #El usuario hizo algo 
            for evento in event.get():
                if evento.type == QUIT :
                    sys.exit()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
