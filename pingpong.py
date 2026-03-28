from pygame import *

window_width = 600 
window_height = 500 
background_color = (175, 225, 175)
window = display.set_mode((window_width, window_height))
window.fill(background_color)

game = True 
finish = False 
clock = time.Clock()
FPS = 60 

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_width, sprite_height, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(sprite_width, sprite_height))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height- 80:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height- 80:
            self.rect.y += self.speed


game_ball = GameSprite('ball.png', 200, 200, 50, 50, 2)

player_right = Player('rightracket.png', 480, 200, 125, 125, 4)

player_left = Player('leftracket.png', 5, 200, 125, 125, 4)

speed_x = 3 
speed_y = 3

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish != True: 
        window.fill(background_color)
        player_right.update_right()
        player_left.update_left()
        game_ball.rect.x += speed_x 
        game_ball.rect.y += speed_y

        if sprite.collide_rect(player_left, game_ball) or sprite.collide_rect(player_right, game_ball):
            speed_x *= -1 
            speed_y *= 1 

        if game_ball.rect.y > window_height-50 or game_ball.rect.y < 0:
            speed_y *= -1

        if game_ball.rect.x > window_width-50 or game_ball.rect.x < 0:
            speed_x *= -1 

    game_ball.reset()
    player_right.reset()
    player_left.reset()
  
    display.update()
    clock.tick(FPS)
