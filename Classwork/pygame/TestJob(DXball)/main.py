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
def Intersect(x1, x2, y1, y2, bx, by):
    if (x1 > x2 - bx) and (x1 < x2 + bx) and (y1 > y2-by) and (y1 < y2+by):
        return True
pygame.init()
size = [900,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('DXBall')
screen.fill(white) #заливаем фон белым цветом
path = os.path.dirname(__file__) #для картинок(это строчка нужна для редактора Atom)
win_img = pygame.image.load(os.path.join(path, 'img/win.jpg'))
lose_img = pygame.image.load(os.path.join(path, 'img/lose.jpg'))
done = True
f1 = pygame.font.Font(None, 36)
Ball = ball()
Ball.x = 350
Ball.y = 400
Ball.change_x = -2
Ball.change_y = -1
Ball.radius = 10
Player1 = player()
bloki = []
raz = 6
bloky = 0
blokx = 0
win = 0
motion = True
spis_x = [100,300,500,700]
wwin = False
lose = False
f1 = pygame.font.Font(None, 36)
for i in range(raz):
    for x in spis_x:
        bloky = bloky + 30
        if bloky == 210:
            bloky = 30
        bloki.append([x,bloky])
        #for tr
print(bloki)
while done:
    screen.fill(white)
    for b in bloki:
        bloks(b[0],b[1])
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False

    # Поведение шарика при соприкосновении с платформой
    if abs(Ball.x > Player1.x - Player1.w) and abs(Ball.x < Player1.x + Player1.w) and abs(Ball.y > Player1.y-Player1.h) and abs(Ball.y < Player1.y+Player1.h):
        Ball.change_y = -1
    # Управление платформой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Player1.x -= 3
    elif keys[pygame.K_RIGHT]:
        Player1.x +=3
    #Поведение блока при попадании на него шарика
    for b in bloki:
        if abs(b[0] - Ball.x) < 100 and abs(b[1] - Ball.y) < 20:
            wwin = True
            bloki.remove(b)
            Ball.change_y = 1
    if wwin:
        win+=1
        wwin=False
    #поведение шарика при ударае об рамки
    if Ball.x > 890:
        Ball.change_x = -2
    elif Ball.x < 10:
        Ball.change_x = 2
    if Ball.y > 600: # Если y будет больше 600, то произойдет конец игры
        lose = True
        motion = False
    elif Ball.y < 10:
        Ball.change_y = 1

    #поведение платвормы при выходе за рамки
    if Player1.x <= -5:
        Player1.x = 800
    elif Player1.x > 800:
        Player1.x = 0
    #Поведение игры, если ты уничтожил все блоки
    if win >= 12:
        screen.blit(win_img,(0,0))
        motion = False
        screen.blit(text1, (350, 500))
    if lose:
        screen.blit(lose_img,(0,0))
        motion = False
        screen.blit(text2, (350, 500))
    if motion: #Прекращение отображения после победы
        Player1.draw(screen)
        Ball.draw(screen)
        Ball.move()
    text1 = f1.render('Количество очков = '+ str(win), 1, (0, 0, 0))
    text2 = f1.render('Количество очков = '+ str(win), 1, (255, 255, 255))
    clock.tick(120)
    pygame.display.flip()
pygame.quit()
