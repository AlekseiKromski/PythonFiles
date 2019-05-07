import pygame
import random
def apple_red(x,y):
       pygame.draw.circle(screen,red,[x,y],20,0)
       pygame.draw.line(screen,black,[x+10,y-30],[x,y-15],5)
def apple_green(x,y):
       poligon_points = [(x,y-50),(x-25,y-20),(x+25,y-20)]
       pygame.draw.circle(screen,green,[x,y],25,0)
       pygame.draw.polygon(screen,red,poligon_points,0)
class Poligon_anti():
    # --- Атрибуты класса --
    # Ball position
    x=0
    y=0
    m=0
    z=0
    # Ball's vector
    change_x=0
    change_y=0
    # Ball size
    size=25
    # Ball color
    color=[255,255,255]
    # --- Методы класса ---
    def move(self):
           self.x += self.change_x
           self.y += self.change_y
    def draw(self, screen):
           pygame.draw.rect(screen, self.color, [self.x, self.y, self.m, self.z],0)
pygame.init()
size = [800,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = True
screen.fill(white)
pygame.display.flip()
STOP = 'stop'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'
UP = 'up'
x = 50 #дял кружка
y = 50 #для кружка
motion = STOP #Нужно для непрерывного движения
ountearv = random.randint(5,15)
ounad = []
radius = 45
ounwin = 0
antiwin = 0
total = 0
win_str = ''
ant_win_str = ''
poligon_anti = Poligon_anti()
poligon_anti.x = 100
poligon_anti.y = 100
poligon_anti.m = 25
poligon_anti.z = 25
poligon_anti.change_x = 2
poligon_anti.change_y = 1
poligon_anti.color = [60,50,155]
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 36)
poligon = True
win = 'none'
for i in range(ountearv):
       ounix = random.randint(50,750)
       ouniy = random.randint(50,550)
       ounad.append([ounix,ouniy])
while done:
       screen.fill(white)
       apple_green(x,y)
       for oun in ounad:
           apple_red(oun[0],oun[1])
       for i in pygame.event.get():
              if i.type == pygame.QUIT:
                     done = False
              elif i.type == pygame.KEYDOWN:
                        if i.key == pygame.K_LEFT:
                                motion = LEFT
                        elif i.key == pygame.K_RIGHT:
                                motion = RIGHT
                        elif i.key == pygame.K_UP:
                                motion = UP
                        elif i.key == pygame.K_DOWN:
                                motion = DOWN
              elif i.type == pygame.KEYUP:
                        if i.key in [pygame.K_LEFT, pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                                motion = STOP
       if motion == LEFT:
              x -= 3
       elif motion == RIGHT:
             x += 3
       elif motion == UP:
              y-=3
       elif motion == DOWN:
              y+=3
       #Не дает выйти за рамки
       if x > 800:
              x = 0
       elif x < 0:
              x = 800
       elif y > 600:
              y = 0
       elif y < 0:
              y = 600
       for oun in ounad:
              if abs(oun[0] - x) < 45 and abs(oun[1] - y) < 45:
                     ounad.remove(oun)
                     ounwin += 1
                     total+=1
       if total == ountearv:
              screen.fill(white)
              text1 = f1.render('Ты съел = '+str(ounwin), 1, (180, 0, 0))
              text2 = f2.render('Соперник съел = '+str(antiwin), 1, (180, 0, 0))
              text3 = f1.render('Победил = '+str(win), 1, (180, 0, 0))
              screen.blit(text1,[100,50])
              screen.blit(text2,[500,50])
              poligon = False
              if ounwin > antiwin:
                     win = 'Ты'
              elif ounwin == antiwin:
                     win = 'Ничья'
              else:
                     win = 'Компьютер'
              screen.blit(text3,[300,400])
              pygame.display.flip()
       if poligon_anti.x > 775 or poligon_anti.x < 25:
               poligon_anti.change_x = poligon_anti.change_x * -1
               #print('x = ',poligon_anti.change_x)
       if poligon_anti.y > 575 or poligon_anti.y < 25:
               poligon_anti.change_y = poligon_anti.change_y * -1
               #print('y = ',poligon_anti.change_y)

       if poligon == True:
              poligon_anti.draw(screen)
              poligon_anti.move()

       for oun in ounad:
              if abs(poligon_anti.x - oun[0]) < 45 and abs(poligon_anti.y - oun[1]) < 45:
                     print(poligon_anti.x,x,poligon_anti.y,y)
                     print(abs(poligon_anti.x - oun[0]),abs(poligon_anti.y - oun[1]))
                     ounad.remove(oun)
                     total+=1
                     antiwin+=1
       clock.tick(120)
       pygame.display.flip()
pygame.quit()
