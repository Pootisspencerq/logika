#Створи власний Шутер!
from typing import Any
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
        bullet =Bullet('bullet.jpg', self.rect.centerx, self.rect.top, 15, 20, 15) 
        bullets.add(bullet)
class Enemy(Gamesprite):
    def update(self):
        self.rect.y+= self.speed
        global lost
        if self.rect.y> win_height:
            self.rect.y =0
            self.rect.x+randint(0, win_width - 80)
            lost =lost +1

class Bullet(Gamesprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()
mixer.init()
mixer_music.load("space.ogg")
mixer_music.play(-1)
mixer.music.set_volume(0.7)
fire_sound = mixer.Sound('fire.ogg')
win_width = 700
win_height=500

font.init()
font1 = font.SysFont('comic sans', 39)
font2 = font.SysFont('papyrus', 39)
txt_lose_game = font2.render("YOU ARE AN IDIOT!!!", 1, (121, 0, 0))
txt_win_game = font2.render("YOU WIN!!!", 1, (0, 159, 74))
txt_lose = font1.render(f'lost: {lost}', 1, (34, 34, 34) )
txt_score = font1.render(f'score: {score}', 1, (34, 34, 34) )
window=display.set_mode((win_width, win_height))
background =scale(image.load('galaxy.jpg'), (win_width, win_height))
ship = Player("rocket.png", 5, win_height - 80, 80, 100, 4)
bullets = sprite.Group()
en = sprite.Group()
for i in range(5):
    e = Enemy("ufo.png", randint(0, win_height -80), 0, 80, 50, randint(1, 5))
    en.add(e)
clock = time.Clock()
FPS = 60
game =1
finish = 0
while game:
    for e in event.get():
        if e.type ==QUIT:
            game = 0    
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
    if not finish:
        window.blit(background, (0, 0))
        txt_lose = font1.render(f'lost: {lost}',1, (255,215,0) )
        window.blit(txt_lose, (10, 50))
        txt_score = font1.render(f'score: {score}',1, (0,0,205) )
        window.blit(txt_score, (10, 10))
        ship.reset()
        en.update()
        en.draw(window)
        ship.update()
        bullets.draw(window)
        
        bullets.update()
       
        
        if (sprite.spritecollide(ship, en, 0)):
            finish = 1
            window.blit(txt_lose_game, (100, 50))
    
    
        collides =sprite.groupcollide(en, bullets, 1, 1)
        for c in collides:
                e = Enemy("ufo.png", randint(0, win_height -80), 0, 80, 50, randint(1, 5))
                en.add(e)
                score = score +1
        if score == 10:
            finish = 1
            window.blit(txt_win_game, (50, 250))
    else:
        finish = 0
        score = 0 
        lost = 0
    
        for b in bullets:
            b.kill()
            
        for e in en:
            e.kill()
        
        time.delay(3000)
        for i in range(5):
            e = Enemy("ufo.png", randint(0, win_height -80), 0, 80, 50, randint(1, 5))
            en.add(e)
    
    display.update()
    clock.tick(FPS)