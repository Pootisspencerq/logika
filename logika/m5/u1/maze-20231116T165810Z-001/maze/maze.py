#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
win_width = 700
win_height=500

window=display.set_mode((win_width, win_height))

background =scale(image.load('background.jpg'), (win_width, win_height))

clock = time.Clock()
FPS = 60
game =1

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type ==QUIT:
            game = 0
    
    display.update()
    clock.tick(FPS)