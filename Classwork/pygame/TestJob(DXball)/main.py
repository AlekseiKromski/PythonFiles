import pygame
import random
import os
class ball():
    x = 0
    y = 0
    change_x = 0
    change_y = 0
    color = [0,0,0]
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),10,10)
class player():
    global green
    def __init__(self,x = 400,y = 500, w = 100,h=10,color = [0,255,0]):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
pygame.init()
size = [800,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
screen.fill(white) #заливаем фон белым цветом
path = os.path.dirname(__file__) #для картинок(это строчка нужна для редактора Atom)
done = True
f1 = pygame.font.Font(None, 36)
Ball = ball()
Ball.x = 400
Ball.y = 500
Ball.change_x = -2
Ball.change_y = -1
Player1 = player()
while done:
    screen.fill(white)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Player1.x -= 3
    elif keys[pygame.K_RIGHT]:
        Player1.x +=3


    if Ball.x > 790:
        Ball.change_x = -2
    elif Ball.x < 10:
        Ball.change_x = 2
    if Ball.y > 600: # Если y будет больше 600, то произойдет конец игры
        screen.fill(black)
        text1 = f1.render('конец игры ',1, white)
        screen.blit(text1,[100,50])
        #для тестов
    elif Ball.y < 10:
        Ball.change_y = 1

    Player1.draw(screen)
    Ball.draw(screen)
    Ball.move()
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
