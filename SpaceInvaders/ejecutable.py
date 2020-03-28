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
    
    def __init__(self,coord_x,coord_y,row,column,color_enable):
        
        super().__init__()

        
        #La variable color_enable, dependiendo de si se encuentra en la primera o última fila lo pinta de un color u otro
        self.color = color_enable

        #Creamos los rectángulos que forman los muros
        self.image = Surface((10,10))
        if self.color == 0 :
            self.image.fill((46,139,87))
        else :
            self.image.fill((67,205,128))
            
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        
        #Obtenemos las coordenadas del rectángulo
        self.rect.x=coord_x
        self.rect.y=coord_y
        
        #Obtenemos su fila y columna
        self.row = row
        self.col = column

    #Getters y setters
    def color (self):
        return self.color
    def color (self,n_color):
        self.color = n_color
    def image (self):
        return self.image
    def image (self,n_image):
        self.image = n_image
    def rect (self):
        return self.rect
    def rect (self,n_rect):
        self.rect = n_rect
    def row (self):
        return self.row
    def row (self,n_row):
        self.row = n_row
    def col (self):
        return self.col
    def col (self,n_col):
        self.col = n_col
    
    
    
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
    
class Alien (sprite.Sprite):
    """Clase que define el comportamiento de un alien"""
    def __init__(self,speed):
        """Iniciamos el objeto"""
        #Iniciando la clase sprite
        super().__init__()
        
        try :
            #Extraenos la imagen para el sprite
            self.image = image.load(GenericData.AL_PATH +"alien.png")
        except FileNotFoundError :
            print("Sprite de alien no encontrado")
            
        #Esta función nos devuelve un objeto con las dimensiones del sprite
        self.rect = self.image.get_rect()
        #Variable para controlar que se mueve izq o drc
        self.dir = 1

        #Velocidad
        assert type(speed) == int ,"Error de tipo en velocidad de alien"
        self.speed = speed
        self.top = 730
        #Atributos para guardar las coordenadas en la animación
        self.changex = 0
        self.changey = 0
        
    def update(self):
        """Método que define el movimiento """
        #Movimiento , de izquierda a derecha y cuando llegamos a una pared descendemos
        if self.rect.x < self.top :
            
            self.rect.x+= self.speed * self.dir
            
        elif self.rect.x > self.top:
            
            self.dir=-1
            self.rect.y +=13
            
        if self.rect.x > 3:
            
            self.rect.x+= self.speed * self.dir
            
        elif self.rect.x < 3:
            
            self.rect.y +=13
            self.dir=1
            
        #Si llegamos a la parte inferior eliminamos el objeto    
        if self.rect.y >=590:
            self.kill()

    #Getters y setters
    def changex (self):
        return self.changex
    def changex (self,n_changex):
        self.changex = n_changex
    def changey (self):
        return self.changey
    def changey (self,n_changey):
        self.changey = n_changey
    def dir (self):
        return self.dir
    def dir (self,n_dir):
        self.dir = n_dir
    def image (self):
        return self.image
    def image (self,n_image):
        self.image = n_image
    def rect (self):
        return self.rect
    def rect (self,n_rect):
        self.rect = n_rect
    def top (self):
        return self.top
    def top (self,n_top):
        self.top = n_top
    def speed (self):
        return self.speed
    def speed (self,n_speed):
        self.speed = n_speed
        
    def burn (self):
        """Método para proporiconar la información para la explosión"""
        #Atributos para guardar las coordenadas en la animación
        return (self.rect.centerx,self.rect.centery)
    
class AlienTocho (Alien):
    """Clase para manejar aliens tochos"""
    def __init__(self,speed):
        """Método para iniciar el alien tocho"""
        super().__init__(speed)
        self.image = image.load(GenericData.AL_PATH +"alien_tocho.png")
        self.rect = self.image.get_rect()
        self.top = 570
        
class Explotion (sprite.Sprite):

    def __init__(self,coord,tipe):
        """Método que inicia el objeto"""
        super().__init__()
        #Si es de alien
        if tipe == 0 :
            try :
                #Extraenos la imagen para la explosión
                self.image = image.load(GenericData.AL_PATH +"explosion.png")
            except FileNotFoundError :
                print("Error en el sprite de la explosión")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
            self.rect.centerx = coord[0]
            self.rect.centery = coord[1]
        #Si es de la nave
        elif tipe == 1 :
            try :
                #Extraenos la imagen para la explosión
                self.image = image.load(GenericData.IMG_PATH +"explosion_ship1.png")
            except FileNotFoundError :
                print("Error en el sprite de la explosión")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
            self.rect.centerx = coord[0]
            self.rect.centery = coord[1]
        elif tipe == 2:
            try :
                #Extraenos la imagen para la explosión
                self.image = image.load(GenericData.AL_PATH +"explosion_tocho.png")
            except FileNotFoundError :
                print("Error en el sprite de la explosión")
            #Esta función nos devuelve un objeto con las dimensiones del sprite
            self.rect = self.image.get_rect()
            self.rect.centerx = 1400#coord[0]
            self.rect.centery = 1200#coord[1]+40
        
        
        #Reloj para controlar el tiempo que se emite
        self.clk = time.get_ticks()
        
        
        
    def update(self):
        """Método para controlar la explosión"""
        #Dejamos un tiempo y eliminamos el objeto
        if (time.get_ticks() - self.clk) > 70 :
            self.kill()
        
        
class SpaceInvaders (GenericData,sprite.Sprite):
    """Clase que se encarga de lanzar el juego"""

    def __init__(self):

        #Configura el título de la ventana
        display.set_caption("Space invaders")
        #Configura el área de la pantalla
        self.screen = display.set_mode((GenericData.AREA))
        try :
            #Preparamos la imagen de fondo
            self.background = image.load(GenericData.BG_PATH + 'background.png').convert_alpha()
        except FileNotFoundError :
            print("No se encuentra el fondo")
        #Inicamos la nave
        self.player = Ship()
        #Creamos un grupo de sprites
        self.spr_list = sprite.Group()
        #Creamos un grupo de balas
        self.bullets_list = sprite.Group()
        #Creamos un grupo de aliens
        self.aliens_list = sprite.Group()
        #Iniciamos el módulo de sonidos
        self.init_sound()
        #Grupo nave
        self.player_list = sprite.Group()
        self.player_list.add(self.player)
        self.spr_list.add(self.player)
        #Reloj
        self.timer = time.get_ticks()
        self.clock = time.Clock()
        #Disparos alien
        self.ab_bullets = sprite.Group()
        self.spr_list_ab = sprite.Group()
        #Contador de vidas
        self.life_counter = 3
        #Contador de score
        self.score_counter = 0
        #Numero de aliens de la ronda
        self.ronda = 5
        #Numero de ronda
        self.num_ronda = 1
        #Incremento de aliens
        self.incremento = 1
        #Tiempo de disparo
        self.shot_time = 550
        #Incremento de velocidad de aliens
        self.speed_ronda = 2
        #Creamos los aliens
        self.create_aliens(self.ronda,self.speed_ronda,False)
        #Grupo muros
        self.wall_group = sprite.Group()
        #iniciamos muros
        self.init_wall()
        #Grupo de explosiones
        self.exp_group = sprite.Group()
        self.image_go= image.load(GenericData.BG_PATH + 'game_over.png')
        self.rect_go = self.image_go.get_rect()
        self.rect_go.centery = 300
        self.rect_go.centerx = 400
        #Alien tocho
        self.difficult_alien = 10
        self.count_alientocho = 0
        
        self.game_over = False
        self.clockgame = time.Clock()
        #contador balas en pantalla
        self.count_bullets_screen=0
        self.clock_bullets = time.Clock()
        self.flag_recharge = False

    #Getter y setter
    def timer(self):
        return self.timer

    def timer(self, new_timer):
        self.timer = new_timer


    def clock(self):
        return self.clock

    def clock(self, new_clock):
        self.clock = new_clock


    def ronda(self):
        return self.ronda

    def ronda(self, new_ronda):
        self.ronda = new_ronda


    def num_ronda(self):
        return self.num_ronda

    def num_ronda(self, new_num_ronda):
        self.num_ronda = new_num_ronda


    def incremento(self):
        return self.incremento

    def incremento(self, new_incremento):
        self.incremento = new_incremento


    def shot_time(self):
        return self.shot_time

    def shot_time(self, new_shot_time):
        self.shot_time = new_shot_time
        

    def speed_ronda(self):
        return self.speed_ronda

    def speed_ronda(self, new_speed_ronda):
        self.speed_ronda = new_speed_ronda


    def difficult_alien(self):
        return self.difficult_alien

    def difficult_alien(self, new_difficult_ronda):
        self.difficult_alien = new_difficult_ronda


    def count_alientocho(self):
        return self.count_alientocho

    def count_alientocho(self, new_alientocho):
        self.count_alientocho = new_alientocho


    def game_over(self):
        return self.game_over

    def game_over(self, new_game_over):
        self.game_over = new_game_over


    def clockgame(self):
        return self.clockgame

    def clockgame(self, new_clockgame):
        self.clockgame = new_clockgame

        
    @property
    def main_music(self):
        return self.__main_music
    
    @main_music.setter
    def main_music(self, new_sound):
        self.__main_music = new_sound


    @property
    def shot_sound(self):
        return self.__shot_sound
    
    @shot_sound.setter
    def shot_sound(self, new_sound):
        self.__shot_sound = new_sound


    @property
    def crash_ship_sound(self):
        return self.__crash_ship_sound
    
    @crash_ship_sound.setter
    def crash_ship_sound(self, new_sound):
        self.__crash_ship_sound = new_sound

    @property
    def crash_alien_sound(self):
        return self.__crash_alien_sound
    
    @crash_alien_sound.setter
    def crash_alien_sound(self, new_sound):
        self.__crash_alien_sound = new_sound
   

    @property
    def restart_sound(self):
        return self.__restart_sound
    
    @restart_sound.setter
    def restart_sound(self, new_sound):
        self.__restart_sound = new_sound
        
    def init_sound (self):
        """Inicializamos música"""
        try :
            #Música
            #Llamamos a la función mixer
            mixer.init()
            #Música de fondo
            self.__main_music = mixer.music.load(GenericData.BG_PATH + 'music.mp3')
            #El -1 indica que está sonando en bucle
            mixer.music.play(-1)
            #Ajustamos el volumen
            mixer.music.set_volume(0.05)
            #Sonido disparo
            self.__shot_sound = mixer.Sound("shot.wav")
            #Sonido explosión alien
            self.__crash_alien_sound = mixer.Sound("ca.wav")
            #Ajustamos el volumen
            mixer.Sound.set_volume(self.__crash_alien_sound,0.1)
            #Sonido explosion nave
            self.__crash_ship_sound = mixer.Sound("cs.wav")
            #Ajustamos el volumen
            mixer.Sound.set_volume(self.__crash_ship_sound,0.1)
            #Sonido explosión final nave
            self.__restart_sound = mixer.Sound("last.wav")
            #Ajustamos el volumen
            mixer.Sound.set_volume(self.__restart_sound,0.1)
        except FileNotFoundError :
            print("Algunos archivos de audio no se han encontrado")
        
    def init_wall(self):
        """Inicializamos los bloques"""
        
        for row in range(5):
            for col in range(15):
                #Primer bloque
                x = 75 + (col * 10)
                y = 435 +  (row * 10)
                #Segundo bloque
                t= 326 + (col * 10)
                s= 435 +  (row * 10)
                #Tercer bloque
                r = 580 + (col * 10)
                w = 435 +  (row * 10)

                #Comprobamos si la fila es la primera o la última para pintarla de otro color
                if row == 0 or row == 4 :
                    
                    wall = Wall(x,y,row,col,0)
                    wall_sec = Wall(t,s,row,col,0)
                    wall_third = Wall(r,w,row,col,0)
                    
                else :
                    
                    wall = Wall(x,y,row,col,1)
                    wall_sec = Wall(t,s,row,col,1)
                    wall_third = Wall(r,w,row,col,1)
                    
                #Añadimos el primer bloque al grupo de bloques (wall_group)
                self.wall_group.add(wall)
                self.screen.blit(wall.image, wall.rect)

                #Añadimos el segundo bloque al grupo de bloques (wall_group)
                self.wall_group.add(wall_sec)
                self.screen.blit(wall_sec.image, wall_sec.rect)

                #Añadimos el tercer bloque al grupo de bloques (wall_group)
                self.wall_group.add(wall_third)
                self.screen.blit(wall_third.image,wall_third.rect)

    def create_aliens (self,alien_num,speed,tocho):
        """Método pa crear aliens"""
        
        if tocho:
            alientocho = AlienTocho(speed)
            alientocho.rect.x = 400
            alientocho.rect.y = 10
            self.aliens_list.add(alientocho)
            
            #alientochodos = AlienTocho(speed)
            #alientochodos.rect.x = 250
            #alientochodos.rect.y = 150
            #self.aliens_list.add(alientochodos)
            
            #Se añaden a la lista de sprites (spr_list)
            self.spr_list.add(alientocho)
            self.screen.blit(alientocho.image,alientocho.rect)
            #Se añaden a la lista de sprites (spr_list)
            #self.spr_list.add(alientochodos)
            #self.screen.blit(alientocho.image,alientochodos.rect)
            
        else:
            for enemy in range(alien_num):
                    #Determina la velocidad de los aliens
                    alien= Alien(speed)
                
                    #Determina la posición de los aliens de forma aleatoria
                    alien.rect.x = random.randint(5,740)
                    alien.rect.y = random.randint(5,300)

                    #Se añaden a la lista de aliens (aliens_list)
                    self.aliens_list.add(alien)

                    #Se añaden a la lista de sprites (spr_list)
                    self.spr_list.add(alien)
                    self.screen.blit(alien.image,alien.rect)
        
    def text (self,vidas):
        """Método para mostrar la puntuación"""
        
        #Iniciando la clase sprite
        super().__init__()

        #Creamos la fuente que vamos a utilizar
        self.font_used = font.Font(None, 59)
        #Le metemos la puntuación
        self.number_score = self.font_used.render(str(self.score_counter), 0, (255, 255, 255))
        self.number_ronda = self.font_used.render(str(self.num_ronda), 0, (255, 255, 255))
        try : 
            #Cargamos el sprite de vidas y lo posicionamos
            self.image_lives = image.load(GenericData.BG_PATH +"lives.png")
            self.rect_lives = self.image_lives.get_rect()
            self.rect_lives.centerx =  500
            self.rect_lives.centery = 20
            #Cargamos el sprite de score y lo posicionamos
            self.image_score = image.load(GenericData.BG_PATH +"score.png")
            self.rect_score = self.image_score.get_rect()
            self.rect_score.centerx =  60
            self.rect_score.centery = 20
            #Cargamos el sprite de round y lo posicionamos
            self.image_round = image.load(GenericData.BG_PATH +"round.png")
            self.rect_round = self.image_round.get_rect()
            self.rect_round.centerx =  320
            self.rect_round.centery = 20
            #Cargamos el primer corazón
            self.image_heart_one = image.load(GenericData.BG_PATH +"heart.png")
            self.rect_heart_one = self.image_heart_one.get_rect()
            self.rect_heart_one.centerx = 580
            self.rect_heart_one.centery = 19
            #Cargamos el segundo corazón
            self.image_heart_two = image.load(GenericData.BG_PATH +"heart.png")
            self.rect_heart_two = self.image_heart_two.get_rect()
            self.rect_heart_two.centerx = 620
            self.rect_heart_two.centery = 19
            #Cargamos el tercer corazón
            self.image_heart_three = image.load(GenericData.BG_PATH +"heart.png")
            self.rect_heart_three = self.image_heart_three.get_rect()
            self.rect_heart_three.centerx = 660
            self.rect_heart_three.centery = 19
        except FileNotFoundError:
            print("Error al cargar los sprites de la cabecera")
            
        #Pegamos la puntuación y las palabras en la pantalla
        self.screen.blit(self.image_lives,self.rect_lives)
        self.screen.blit(self.image_score,self.rect_score)
        self.screen.blit(self.image_round,self.rect_round)
        self.screen.blit(self.number_score,(120,4))
        self.screen.blit(self.number_ronda,(380,3))

        #Comprobamos el contador de vidas para saber cuantos corazones pintar
        if vidas > 0:
            
            self.screen.blit(self.image_heart_one,self.rect_heart_one)
            
        if vidas > 1 :
            
            self.screen.blit(self.image_heart_two,self.rect_heart_two)
            
        if vidas == 3  :
            
            self.screen.blit(self.image_heart_three,self.rect_heart_three)

        #Pintamos el cargador
        self.image_recharge0 = image.load(GenericData.BG_PATH +"recarga_0.png")
        self.rect_recharge0 = self.image_recharge0.get_rect()
        self.rect_recharge0.centerx =  736
        self.rect_recharge0.centery = 30
        self.image_recharge1 = image.load(GenericData.BG_PATH +"recarga_1.png")
        self.rect_recharge1 = self.image_recharge1.get_rect()
        self.rect_recharge1.centerx =  736
        self.rect_recharge1.centery = 30
        self.image_recharge2 = image.load(GenericData.BG_PATH +"recarga_2.png")
        self.rect_recharge2 = self.image_recharge2.get_rect()
        self.rect_recharge2.centerx = 736
        self.rect_recharge2.centery = 30
        self.image_recharge3 = image.load(GenericData.BG_PATH +"recarga_3.png")
        self.rect_recharge3 = self.image_recharge3.get_rect()
        self.rect_recharge3.centerx =  736
        self.rect_recharge3.centery = 30
        self.image_recharge4 = image.load(GenericData.BG_PATH +"recarga_4.png")
        self.rect_recharge4 = self.image_recharge4.get_rect()
        self.rect_recharge4.centerx =  736
        self.rect_recharge4.centery =30
        self.image_recharge5 = image.load(GenericData.BG_PATH +"recarga_5.png")
        self.rect_recharge5 = self.image_recharge5.get_rect()
        self.rect_recharge5.centerx =  736
        self.rect_recharge5.centery = 30
            
        if self.count_bullets_screen == 0 or self.count_bullets_screen < 2:
            self.screen.blit(self.image_recharge5,self.rect_recharge5)
        elif self.count_bullets_screen == 2 or  self.count_bullets_screen == 3:
            self.screen.blit(self.image_recharge4,self.rect_recharge4)
        elif self.count_bullets_screen == 4 or self.count_bullets_screen == 5:
            self.screen.blit(self.image_recharge3,self.rect_recharge3)
        elif self.count_bullets_screen == 6 or self.count_bullets_screen == 7:
            self.screen.blit(self.image_recharge2,self.rect_recharge2)
        elif self.count_bullets_screen == 8:
            self.screen.blit(self.image_recharge1,self.rect_recharge1)
        elif self.count_bullets_screen > 8:
            self.screen.blit(self.image_recharge0,self.rect_recharge0)
            
    def redraw(self):
        """Método para redibujar los objetos una vez actualizados y conseguir el efecto juego"""
        #Ponemos el fondo
        self.screen.blit(self.background, (0, 0))
        if self.game_over == False :
            #Pintamos la nave
            self.screen.blit(self.player.image,self.player.rect)
            #Pintamos la cabecera
            self.screen.blit(self.image_lives,self.rect_lives)
            self.screen.blit(self.image_score,self.rect_score)
            self.screen.blit(self.image_round,self.rect_round)
            self.screen.blit(self.number_score,(120,4))
            self.screen.blit(self.number_ronda,(380,3))
            #Pintamos corazones        
            if self.life_counter > 0:
            
                self.screen.blit(self.image_heart_one,self.rect_heart_one)
            
            if self.life_counter > 1:
            
                self.screen.blit(self.image_heart_two,self.rect_heart_two)
            
            if self.life_counter == 3 :
            
                self.screen.blit(self.image_heart_three,self.rect_heart_three)

            if self.count_bullets_screen == 0 or self.count_bullets_screen < 2:
                self.screen.blit(self.image_recharge5,self.rect_recharge5)
            elif self.count_bullets_screen == 2 or  self.count_bullets_screen == 3:
                self.screen.blit(self.image_recharge4,self.rect_recharge4)
            elif self.count_bullets_screen == 4 or self.count_bullets_screen == 5:
                self.screen.blit(self.image_recharge3,self.rect_recharge3)
            elif self.count_bullets_screen == 6 or self.count_bullets_screen == 7:
                self.screen.blit(self.image_recharge2,self.rect_recharge2)
            elif self.count_bullets_screen == 8:
                self.screen.blit(self.image_recharge1,self.rect_recharge1)
            elif self.count_bullets_screen > 8:
                self.screen.blit(self.image_recharge0,self.rect_recharge0)
                
            #Recorremos aliens pegando
            for j in self.aliens_list:
                self.screen.blit(j.image, j.rect)
            #Recorremos balas pegando   
            for i in self.bullets_list:
                self.screen.blit(i.image, i.rect)
            #Recorremos balas aliens pegando   
            for k in self.ab_bullets:
                self.screen.blit(k.image, k.rect)
            #Recorremos muros pegando
            for l in self.wall_group:
                self.screen.blit(l.image, l.rect)
            #Recorremos explosiones pegando y actualizandolas
            for m in self.exp_group:
                m.update()
                self.screen.blit(m.image,m.rect)
        else  :
            
            self.screen.blit(self.image_go,self.rect_go)
            
           
            
        #Actualizamos pantalla
        display.update()
        
    def ship_shoot(self):
        """Método para que la nave dispare"""
        
       
        if self.flag_recharge:
            if (time.get_ticks() - self.clock_bullets) < 2000:
                pass
            else :
                self.count_bullets_screen = 0
                self.flag_recharge = False
        else :
            #Recogemos los eventos
            events = event.get()

            #Controlamos el boton espacio para disparar
            for even in events:
                if even.type == KEYDOWN:
                    if even.key == K_SPACE:

                        #Activamos sonido de disparo
                        mixer.Sound.play(self.__shot_sound)
                        #Creamos la bala
                        bullet = Bullet(self.player.rect.centerx,self.player.rect.top,-1,22,1)
                        #Añadimos la bala al contador de balas en pantalla
                        self.count_bullets_screen+=1
                        #Añadimos la bala a la lista de balas
                        self.bullets_list.add(bullet)
                        #Añadimos la bala a la lista de sprites
                        self.spr_list.add(bullet)
                        #Pegamos la bala a la pantalla
                        self.screen.blit(bullet.image, bullet.rect)
                        if self.count_bullets_screen == 9 :
                            self.flag_recharge = True
                            self.clock_bullets = time.get_ticks()

                    

    def alien_shoot(self):
        """Método para que la nave dispare"""
        
    
        #Disminuimos el tiempo entre disparos con el tiempo
        if self.shot_time > 200 and self.ronda >15:
            self.shot_time -=50
        #Si ha pasado el tiempo    
        if (time.get_ticks() - self.timer) > self.shot_time:
            #Creamos una lista con los aliens para elegir uno
            self.a_list = self.aliens_list.sprites()
            tam = len(self.a_list)
            if tam != 0:
                #Elegimos un alien al azar para que dispare
                alien = self.a_list[randrange(tam)]
                #Si es el alien final
                if isinstance(alien,AlienTocho):
                    bullet = Bullet(alien.rect.centerx+50,alien.rect.bottom ,1,10,0)
                    bullet_two = Bullet(alien.rect.centerx-50,alien.rect.bottom ,1,10,0)
                    #Añadimos la bala a la lista de balas
                    self.ab_bullets.add(bullet)
                    self.ab_bullets.add(bullet_two)
                    #Añadimos la bala a la lista de sprites
                    self.spr_list_ab.add(bullet)
                    self.spr_list_ab.add(bullet_two)
                    #Pegamos la bala a la pantalla
                    self.screen.blit(bullet.image, bullet.rect)
                    self.screen.blit(bullet.image, bullet_two.rect)
                    #Volvemos a tomar el tiempo
                    self.timer = time.get_ticks() 

                else :
                    #Si es un alien normal
                    #Creamos la bala
                    bullet = Bullet(alien.rect.centerx,alien.rect.bottom +5,1,10,0)
                    #Añadimos la bala a la lista de balas
                    self.ab_bullets.add(bullet)
                    #Añadimos la bala a la lista de sprites
                    self.spr_list_ab.add(bullet)
                    #Pegamos la bala a la pantalla
                    self.screen.blit(bullet.image, bullet.rect)
                    #Volvemos a tomar el tiempo
                    self.timer = time.get_ticks()

    def colitions (self):
            #Colisiones aliens con balas
            for bullet in self.bullets_list:
                
                #Obtenemos los aliens 
                alien_shot = sprite.spritecollide(bullet, self.aliens_list, False)
                for alien in alien_shot:
                    if isinstance(alien,AlienTocho) :
                        
                        #Hacemos una explosion
                        exp = Explotion(alien.burn(),2)
                        self.exp_group.add(exp)
                        #Ponemos el sonido de la explosión
                        mixer.Sound.play(self.__crash_alien_sound)
                        #Borramos las balas
                        self.count_alientocho+=1
                        self.bullets_list.remove(bullet)
                        self.spr_list.remove(bullet)
                        if self.count_alientocho > self.difficult_alien :
                            self.difficult_alien+=4
                            self.aliens_list.remove(alien)
                            alien.kill()
                            self.count_alientocho = 0
                    else :
                        #Hacemos que exploten
                        exp = Explotion(alien.burn(),0)
                        self.exp_group.add(exp)
                        #Ponemos el sonido de la explosión
                        mixer.Sound.play(self.__crash_alien_sound)
                        #Aumentamos la puntuación
                        self.score_counter+=50
                        #Borramos las balas
                        self.bullets_list.remove(bullet)
                        self.spr_list.remove(bullet)
                        self.spr_list.remove(alien)
                        self.aliens_list.remove(alien)
                        alien.kill()
                #Si matamos a todos los aliens     
                self.a_list = self.aliens_list.sprites()
                tam = len(self.a_list)
                if tam == 0:
                    if self.ronda < 50:
                        #Aumentamos el número de aliens 
                        self.ronda += self.incremento
                        #Aumentamos su velocidad
                    if self.speed_ronda <8 and self.ronda >9:
                        self.speed_ronda +=1
                        
                    #Eliminamos las balas
                    for bala in self.ab_bullets:
                        self.ab_bullets.remove(bala)
                    for disparo in self.bullets_list:
                        self.bullets_list.remove(disparo)
                    #Restablecemos flags de recarga   
                    self.count_bullets_screen = 0
                    self.flag_recharge = False
                    self.num_ronda += 1
                    #Volvemos a empezar
                    if self.num_ronda %5 == 0:
                        self.create_aliens(self.ronda,self.speed_ronda,True)
                    else :
                        self.create_aliens(self.ronda,self.speed_ronda,False)
                    #Colocamos los muros de nuevo
                    self.init_wall()
                        
            #Colisiones balas con balas
            sprite.groupcollide(self.bullets_list, self.ab_bullets, True, True)
            
            #Colisiones  muros
            sprite.groupcollide(self.bullets_list, self.wall_group, True, True)
            sprite.groupcollide(self.ab_bullets, self.wall_group, True, True)
            
            sprite.groupcollide(self.aliens_list, self.wall_group, False, True)
            
            #Colisiones nave con balas
            for bullet in self.ab_bullets:
                if self.life_counter > 1:
                    
                    player_shot = sprite.spritecollide(bullet, self.player_list,False)
                    
                    for player in player_shot:
                        #Ponemos explosion
                        exp = Explotion(player.burn(),1)
                        self.exp_group.add(exp)
                        #Ponemos el sonido
                        mixer.Sound.play(self.__crash_ship_sound)
                        #Quitamos una vida
                        self.life_counter-=1
                        #Borramos balas
                        self.ab_bullets.remove(bullet)
                        self.spr_list_ab.remove(bullet)
                else :
                    
                    player_shot = sprite.spritecollide(bullet, self.player_list,False)
                    for player in player_shot:
                        mixer.Sound.play(self.__restart_sound)
                        self.life_counter=3
            
                        #Si perdemos, quitamos los aliens y exp
                        for a in self.aliens_list:
                            self.aliens_list.remove(a)
                        for ep in self.exp_group:
                            self.exp_group.remove(ep)      
                        

                        #Eliminamos las balas
                        self.ab_bullets.remove(bullet)
                        self.spr_list_ab.remove(bullet)
                        for shot in self.ab_bullets:
                            self.ab_bullets.remove(shot)
                        for disparo in self.bullets_list:
                            self.bullets_list.remove(disparo)


                        self.game_over = True   
                        #Y volvemos a empezar
                        self.shot_time = 550
                        self.ronda = 5
                        self.speed_ronda = 2
                        self.create_aliens(self.ronda,self.speed_ronda,False)
                        self.player.rect.centerx = 400
                        self.player.rect.centery = 565
                        #Restablecemos score
                        self.score_counter= 0
                        self.num_ronda = 1
                        #Restablecemos flags de recarga   
                        self.count_bullets_screen = 0
                        self.flag_recharge = False
                        #Colocamos los muros de nuevo
                        self.init_wall()
                        
                        
            #Colisiones alien-nave
            for ali in self.aliens_list:
                if self.life_counter > 1:
                    
                    player_shot = sprite.spritecollide(ali, self.player_list,False)
                    for player in player_shot:
                        if isinstance(ali,AlienTocho):
                            #Si chocamos con el alientocho volvemos a empezar
                            #Sonido
                            mixer.Sound.play(self.__restart_sound)
                            self.life_counter=3
                        
                            #Si perdemos, quitamos los aliens y explosiones
                            for a in self.aliens_list:
                                self.aliens_list.remove(a)
                            for ep in self.exp_group:
                                self.exp_group.remove(ep)
                            #Quitamos las balas
                            #Eliminamos las balas
                            for bala in self.ab_bullets:
                                self.ab_bullets.remove(bala)
                            for disparo in self.bullets_list:
                                self.bullets_list.remove(disparo)
                            
                            self.game_over = True
                        
                            #Y volvemos a empezar
                            #Restablecemos flags de recarga   
                            self.count_bullets_screen = 0
                            self.flag_recharge = False
                            self.shot_time = 550
                            self.ronda = 5
                            self.speed_ronda = 2
                            self.create_aliens(self.ronda,self.speed_ronda,False)
                            self.player.rect.centerx = 400
                            self.player.rect.centery = 565
                            #Restablecemos score
                            self.score_counter= 0
                            self.num_ronda = 1
                            #Colocamos los muros de nuevo
                            self.init_wall()
                        else:
                            #Ponemos explosion nave
                            exp = Explotion(player.burn(),1)
                            self.exp_group.add(exp)
                            #Ponemos explosion alien
                            exp = Explotion(ali.burn(),0)
                            self.exp_group.add(exp)
                            #Sonido de explosión
                            mixer.Sound.play(self.__crash_ship_sound)
                            #Quitamos una vida del contador
                            self.life_counter-=1
                            #Borramos el alien
                            self.aliens_list.remove(ali)
                            self.spr_list.remove(ali)
                else  :
                    
                    player_shot = sprite.spritecollide(ali, self.player_list,False)
                    for player in player_shot:
                        
                        #Sonido
                        mixer.Sound.play(self.__restart_sound)
                        self.life_counter=3
                        
                        #Si perdemos, quitamos los aliens y explosiones
                        for a in self.aliens_list:
                            self.aliens_list.remove(a)
                        for ep in self.exp_group:
                            self.exp_group.remove(ep)
                        #Quitamos las balas
                        #Eliminamos las balas
                        for bala in self.ab_bullets:
                            self.ab_bullets.remove(bala)
                        for disparo in self.bullets_list:
                            self.bullets_list.remove(disparo)
                            
                        self.game_over = True
                        
                        #Y volvemos a empezar
                        self.shot_time = 550
                        self.ronda = 5
                        self.speed_ronda = 2
                        #Restablecemos flags de recarga   
                        self.count_bullets_screen = 0
                        self.flag_recharge = False
                        self.create_aliens(self.ronda,self.speed_ronda,False)
                        self.player.rect.centerx = 400
                        self.player.rect.centery = 565
                        #Restablecemos score
                        self.score_counter= 0
                        self.num_ronda = 1
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
            
            #Se vuelve a llamar al método para disparar para mejorar el funcionamiento del disparo
            self.ship_shoot()
            
            #Controlamos las colisiones entre objetos
            self.colitions()
            
            #Se vuelve a llamar al método para disparar para mejorar el funcionamiento del disparo
            self.ship_shoot()
            
            #Añadimos el texto a la pantalla          
            self.text(self.life_counter)
            
            self.clockgame = time.get_ticks()
            if self.game_over == True:
                
                while (time.get_ticks()-self.clockgame+450) < 3555 :
                    #Método para redibujar la pantalla y que funcione el movimiento
                    if (time.get_ticks()-self.clockgame+450)%500 == 0:
                         self.rect_go.centery = 1600
                         self.rect_go.centerx = 1899
                         self.redraw()
                    elif(time.get_ticks()-self.clockgame+450)%755 == 0:
                        self.rect_go.centery = 300
                        self.rect_go.centerx = 400
                        self.redraw()
                        
                self.game_over = False
            
            else:
                #Método para redibujar la pantalla y que funcione el movimiento
                self.redraw()

            #Se vuelve a llamar al método para disparar para mejorar el funcionamiento del disparo
            self.ship_shoot()
            
            #El usuario hizo algo 
            for evento in event.get():
                if evento.type == QUIT :
                    sys.exit()
            
if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
