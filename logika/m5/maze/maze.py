#створи гру "Лабіринт"!
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed) -> None:
        super().__init__()
        self.image = scale(load(player_image), (65,65))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x =player_x
        self.rect.y =player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    
win_width = 700
win_height=500

window=display.set_mode((win_width, win_height))

background =scale(image.load('background.jpg'), (win_width, win_height))
player = gamesprite("hero.png", 5, win_height - 80, 4)
evil = gamesprite("cyborg.png", win_width - 115, win_height - 280, 3 )
clock = time.Clock()
FPS = 60
game =1
mixer.init()
mixer_music.load("jungles.ogg")
mixer_music.play()
while game:
    window.blit(background, (0, 0))
    player.reset()
    evil.reset()
    
    for e in event.get():
        if e.type ==QUIT:
            game = 0
    
    display.update()
    clock.tick(FPS)