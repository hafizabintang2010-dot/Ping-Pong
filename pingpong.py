from pygame import *

window_width = 600 
window_height = 500 
background_color = (175, 225, 175)
window = display.set_mode((window_width, window_height))
window.fill(background_color)

game = True 
clock = time.Clock()
FPS = 60 
while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False 

    display.update()
    clock.tick(FPS)
