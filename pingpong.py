from pygame import *

window_width = 600 
window_height = 500 
background_color = (175, 225, 175)
window = display.set_mode((window_width, window_height))
window.fill(background_color)

game = True 
clock = time.Clock()
FPS = 60 

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_width, sprite_height, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(sprite_width, sprite_height))
        self.speed = sprite_speed
        self.rectangle = self.image.get_rect()
        self.rectangle.x = sprite_x
        self.rectangle.y = sprite_y

    def reset(self): 
        window.blit(self.image, (self.rectangle.x, self.rectangle.y))

game_ball = GameSprite('ball.png', 200, 200, 50, 50, 4)

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False 

    game_ball.reset()

    display.update()
    clock.tick(FPS)
