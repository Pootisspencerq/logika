#створи гру "Лабіринт"!
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed) -> None:
        super().__init__()
        self.image = scale(load(player_image), (65,65))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x =player_x
        self.rect.y =player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    
        
class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys [K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed    
            
        if keys [K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed   
            
            
class Enemy(Gamesprite):      
    direction = 'left'
    def update(self):
        if self.direction == 'left' and self.rect.x:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed  
            
             
        if  self.rect.x <=450:
            self.direction = 'right'  
        if  self.rect.x >=win_width -80:
            self.direction = 'left'  
            
            
class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_widht, wall_height ):
        super().__init__()
        self.widht= wall_widht
        self.height= wall_height
                  
        
        self.image = Surface((self.widht, self.height)) 
        self.image.fill((0, 225, 0)) 
        
        self.rect = self.image.get_rect()
        self.rect.x =wall_x
        self.rect.y =wall_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))          
win_width = 700
win_height=500

window=display.set_mode((win_width, win_height))

background =scale(image.load('background.jpg'), (win_width, win_height))
player = Player("hero.png", 5, win_height - 80, 4)
evil = Enemy("cyborg.png", win_width - 115, win_height - 280, 3 )
treasure =Gamesprite('treasure.png', win_width-80,win_height-80, 0)
wall=Wall(10, 10, 200, 100)
wall2=Wall(15, 10, 100, 200)

walls = [wall, wall2]


clock = time.Clock()
FPS = 60
game =1
finish = 0

font.init()
f = font.Font(None, 70)

win = f.render('YOURE A WINNER!', True, (225, 215, 0))
lose = f.render('YOURE A LOSER!', True, (225, 0, 0))
mixer.init()
mixer_music.load("jungles.ogg")
mixer_music.play()

money_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')
while game:
    for e in event.get():
        if e.type ==QUIT:
            game = 0
            
    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        evil.reset()
        treasure.reset()
        wall.reset()
        wall2.reset()
        
        player.update()
        evil.update()
        if sprite.collide_rect(player, treasure):
            finish = 1
            window.blit(win, (200, 200))
            money_sound.play()
            
        if sprite.collide_rect(player, evil) or sprite.collide_rect(player, wall) :
            finish = 1
            window.blit(lose, (200, 200))
            money_sound.play() 
        for wall in walls:
            if sprite.collide_rect(player, wall):
                finish = True
                window.blit(lose, (200, 200))
                kick_sound.play()
    display.update()
    clock.tick(FPS)