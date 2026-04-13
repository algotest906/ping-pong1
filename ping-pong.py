from pygame import *
from random import randint
import time
total = 0
wait = 0
init()
window = display.set_mode((700, 500))
BACK = (200,255,255)
clock = Clock()
cards = list()
x = 20

window.fill(BACK)

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 10:
            self.rect.x += self.speed_y
        if keys_pressed[K_s] and self.rect.y > 590:
            self.rect.x -= self.speed_y

    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y < 10:
            self.rect.x += self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y > 590:
            self.rect.x -= self.speed_y

class Area():
    def __init__(self,x,y,width,height,colors):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = colors

    def set_color(self,colors):
        self.fill_color = colors

    def f_color(self):
        pygame.draw.rect(window,self.fill_color,self.rect)

    def obvodka(self,colors):
        pygame.draw.rect(window,colors,self.rect,5)

    def colliderect(self,rect):
        return self.rect.colliderect(rect)

ball = Gamesprite('ball.png',325,275,50,50,3,3)
platform1 = Player('platform.png',10,300,20,100,0,5)
platform2 = Player('platform.png',670,300,20,100,0,5)

while not game_over:
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.update()
    ball.reset()
    platform1.update_left()
    platform1.reset()
    platform2.update_right()
    platform2.reset()
    display.update()
    clock.tick(60)