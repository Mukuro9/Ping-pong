from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, hight, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        okienko.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_right(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < okie_hight - 80:
            self.rect.y += self.speed
    def move_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < okie_hight - 80:
            self.rect.y += self.speed

okie_width = 700
okie_hight = 1000
okienko = display.set_mode((okie_hight, okie_width))
background = transform.scale(image.load('background3.png'), (okie_hight, okie_width))

racketa1 = Player('racket.png', 10, 200, 50, 100, 15)
racketa2 = Player('racket.png', 960, 200, 50, 100, 15)
ball = GameSprite('tenis_ball.png', 500, 200, 70, 70, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('ИГРОК 1 ПРОИГРАЛ', True, (249, 49, 33))
lose2 = font.render('ИГРОК 2 ПРОИГРАЛ', True, (249, 49, 33))

speed_y = 3
speed_x = 3

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        okienko.blit(background, (0, 0))
        racketa1.move_left()
        racketa2.move_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racketa1, ball) or sprite.collide_rect(racketa2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > okie_width-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            okienko.blit(lose1, (400, 200))

        if ball.rect.x > okie_hight:
            finish = True
            okienko.blit(lose2, (400, 200))

        racketa1.reset()
        racketa2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)




