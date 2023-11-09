from pygame import *

window = display.set_mode((700, 500))
background = transform.scale(image.load('background.png'), (700, 500))
clock = time.Clock()
FPS = 60

speed = 10

chra1 = transform.scale(image.load('sprite1.png'), (100, 100))
x1 = 100 
y1 =400
chra2 = transform.scale(image.load('sprite2.png'), (100, 100))
x2=300  
y2=300


game = 1

while game:
    window.blit(background, (0, 0))
    window.blit(chra1, (x1, y1))
    window.blit(chra2, (x2, y2))
    
    for e in  event.get():
        if e.type ==QUIT:
            game = 0
        
    keys_pressed = key.get_pressed() 
    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= speed
        
    if keys_pressed[K_RIGHT] and x1 < 600:
        x1 += speed
        keys_pressed = key.get_pressed() 
        
    if keys_pressed[K_UP] and y1 > 0:
        y1 -= speed
        
    if keys_pressed[K_DOWN] and y1 < 400:
        y1 += speed  
    keys_pressed = key.get_pressed() 
    
    
    if keys_pressed[K_a] and x2 > 0:
        x2 -= speed
        
    if keys_pressed[K_d] and x2 < 600:
        x2 += speed
        keys_pressed = key.get_pressed() 
        
    if keys_pressed[K_w] and y2 > 0:
        y2 -= speed
        
    if keys_pressed[K_s] and y2 < 400:
        y2 += speed              
    display.update()
    clock.tick(FPS)