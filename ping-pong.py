from pygame import *
from random import randint
total = 0
wait = 0
init()
window = display.set_mode((700, 500))
BACK = (200,255,255)
clock = time.Clock()
cards = list()
x = 20
game_over = False

window.fill(BACK)

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed_x, speed_y, colors):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.colors = colors

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def f_color(self):
        draw.rect(window, self.colors, self.rect)

    def touch(self):
        if self.rect.colliderect(platform1) or self.rect.colliderect(platform2):
            self.speed_x *= -1
        if self.rect.y <= 1 or self.rect.y > 449:
            self.speed_y *= -1

class Player(Gamesprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 390:
            self.rect.y += self.speed_y
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed_y

    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed_y
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed_y

    def f_color(self):
        draw.rect(window, self.colors, self.rect)

    def touch(self):
        if self.rect.colliderect(platform1) or self.rect.colliderect(platform2):
            self.speed_x *= -1
        if self.rect.y <= 1 or self.rect.y > 449:
            self.speed_y *= -1

class Area():
    def __init__(self ,x , y ,width ,height ,colors):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = colors

    def set_color(self,colors):
        self.fill_color = colors

    def f_color(self):
        pygame.draw.rect(window, self.colors, self.rect)

    def obvodka(self,colors):
        pygame.draw.rect(window, colors, self.rect, 5)

    def colliderect(self,rect):
        return self.rect.colliderect(rect)

ball = Gamesprite('tenis_ball.png',325,350,50,50,3,-3,BACK)
platform1 = Player('racket.png',10,300,20,100,0,5,BACK)
platform2 = Player('racket.png',670,300,20,100,0,5,BACK)

while not game_over:
    for e in event.get():
        if e.type == QUIT:
            game_over = True
    ball.f_color()
    platform1.f_color()
    platform2.f_color()
    ball.update()
    ball.reset()
    platform1.update_left()
    platform1.reset()
    platform2.update_right()
    platform2.reset()
    display.update()
    ball.touch()
    platform1.touch()
    platform2.touch()
    #if ball.rect.x <= 1 or ball.rect.x => 649:

    clock.tick(60)