#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
lost = 0
score = 0
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed) -> None:
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x =player_x
        self.rect.y =player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    
        
class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed    
            
        if keys [K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed   

    def fire(self):
        pass  
      
class Enemy(Gamesprite):
    def update(self):
        self.rect.y+= self.speed
        global lost
        if self.rect.y> win_height:
            self.rect.x =0
            self.rect.y+randint(- 45, 50)
            lost =lost +1


mixer.init()
mixer_music.load("space.ogg")
mixer_music.play(-1)
mixer.music.set_volume(0.7)
win_width = 700
win_height=500

window=display.set_mode((win_width, win_height))
background =scale(image.load('galaxy.jpg'), (win_width, win_height))
ship = Player("rocket.png", 5, win_height - 80, 80, 100, 4)
en = Sprite.groups()
for i in range(5):
    en = Enemy("ufo.png", randint(0, win_height -80), 0, 80, 50, randint(1, 5))
clock = time.Clock()
FPS = 60
game =1
finish = 0
while game:
    for e in event.get():
        if e.type ==QUIT:
            game = 0    
    
    if not finish:
        window.blit(background, (0, 0))
        ship.reset()
        en.update()
        en.draw(window)
        ship.update()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    display.update()
    clock.tick(FPS)