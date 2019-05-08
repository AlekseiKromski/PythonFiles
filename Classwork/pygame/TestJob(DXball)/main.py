import pygame
import random
import os
class ball():
    x = 0
    y = 0
    change_x = 0
    change_y = 0
    radius = 10
    color = [0,0,0]
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
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
def bloks(x,y):
       pygame.draw.rect(screen,red,(x,y,100,20))
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
Ball.y = 400
Ball.change_x = -2
Ball.change_y = -1
Ball.radius = 10
Player1 = player()
bloki = []
raz = 6
bloky = 0
blokx = 20
spis_x = [20,180,340,500]
for i in range(raz):
    for x in spis_x:
        bloky = bloky + 30
        if bloky == 180:
            bloky = 30
            blokx = x
        bloki.append([blokx,bloky])
        #for tr
print(bloki)
while done:
    screen.fill(white)
    for b in bloki:
        bloks(b[0],b[1])
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    # Управление платформой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Player1.x -= 3
    elif keys[pygame.K_RIGHT]:
        Player1.x +=3

    #Поведение блока при попадании на него шарика
    for b in bloki:
        if abs(b[0] - Ball.x) < 100 and abs(b[1] - Ball.y) < 20:
            bloki.remove(b)
            #test
            Ball.change_y = 1


    #поведение шарика при ударае об рамки
    if Ball.x > 790:
        Ball.change_x = -2
    elif Ball.x < 10:
        Ball.change_x = 2
    if Ball.y > 600: # Если y будет больше 600, то произойдет конец игры
        screen.fill(black)
        text1 = f1.render('конец игры ',1, white)
        screen.blit(text1,[100,50])
    elif Ball.y < 10:
        Ball.change_y = 1
    #поведение шарика при прекосновении об платформу
    '''
    НУЖНА КОНСУЛЬТАЦИЯ УЧИТЕЛЯ!!!
    '''
    #поведение платвормы при выходе за рамки
    if Player1.x < -100:
        Player1.x = 700
    elif Player1.x > 790:
        Player1.x = 10

    Player1.draw(screen)
    Ball.draw(screen)
    Ball.move()
    clock.tick(120)
    pygame.display.flip()
pygame.quit()
