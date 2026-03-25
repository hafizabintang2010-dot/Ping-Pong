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

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rectangle.y > 5:
            self.rectangle.y -= self.speed
        if keys[K_DOWN] and self.rectangle.y < window_height- 80:
            self.rectangle.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rectangle.y > 5:
            self.rectangle.y -= self.speed
        if keys[K_s] and self.rectangle.y < window_height- 80:
            self.rectangle.y += self.speed


game_ball = GameSprite('ball.png', 200, 200, 50, 50, 4)

player_right = Player('racket.png', 480, 200, 150, 150, 4)

player_left = Player('racket.png', 5, 200, 150, 150, 4)

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False 

    window.fill(background_color)
    game_ball.reset()
    player_right.reset()
    player_right.update_right()
    player_left.reset()
    player_left.update_left()

    display.update()
    clock.tick(FPS)
