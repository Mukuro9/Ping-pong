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
        if keys[K_d] and self.rect.y < okie_heigth - 80:
            self.rect.y += self.speed
    def move_left(self):
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < okie_heigth - 80:
            self.rect.y += self.speed

okie_width = 1050
okie_hight = 800
okienko = display.set_mode(okie_hight, okie_width)
background = transform.scale(image.load('background.jpg'), (okie_width, okie_hight))

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 150)

font.init()
font = font.Font(None, 35)
lose1 = font.render('ИГРОК 1 ПРОИГРАЛ', True, (249, 49, 33))
lose2 = font.render('ИГРОК 2 ПРОИГРАЛ', True, (249, 49, 33))