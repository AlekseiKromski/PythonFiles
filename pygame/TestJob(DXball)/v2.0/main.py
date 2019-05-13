import pygame
import os #Добавление этого модуля не обязательно, но он нужен для редактора кода Atom
class ball(): #Класс шарика, по котору будет создоваться объект(Шарик)
    x = 0
    y = 0
    change_x = 0 #Изменение движение шарика по оси x
    change_y = 0 #Изменение движение шарика по оси y
    radius = 10
    color = [0,0,0]
    def move(self): #Движение шарика
        '''
        В основном изменение change_x, change_y будут происходить при отталкивании об стенки рамки, блоков, платформы(игрока)
        '''
        self.x += self.change_x
        self.y += self.change_y
    def draw(self,screen): # Отрисовка шарика
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

class player(): #Класс игрока, на основе этого будет создан объект Player1
    def __init__(self,x = 400,y = 500, w = 100,h=10,color = [0,0,0]): #стандартные значения для игрока (их можно поменять, при создании класса)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self,screen,player_texture):
        #pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h)) #Нужно для тестов
        screen.blit(player_texture,(self.x,self.y))


def bloks(x,y,block_texture,screen): #создание блоков
       #pygame.draw.rect(screen,red,(x,y,100,20))
       screen.blit(block_texture,(x,y))

def ball_texture_draw(screen,x,y):
    if ball_activated:
        screen.blit(ball_texture_activated,(x,y))
    else:
        screen.blit(ball_texture,(x,y))
def play():
    def bloks(x,y,block_texture,screen): #создание блоков
           #pygame.draw.rect(screen,red,(x,y,100,20))
           screen.blit(block_texture,(x,y))
    global bloki
    global block_texture
    global screen
    global motion
    global bloky
    global spis_x
    global ball_activated
    global win
    global lose_sound_play
    global win_sound_play
    Ball.x = 350
    Ball.y = 400
    Ball.change_x = -2
    Ball.change_y = -1
    motion = True
    ball_activated = True
    win = 0
    pygame.mixer.music.play()
    lose_sound_play = True
    win_sound_play = True
    for i in range(raz): #Создаем двоичный массив, в котором будет храниться расположение каждого блока
        for x in spis_x:
            bloky = bloky + 30
            if bloky == 210:
                bloky = 30
            bloki.append([x,bloky])
    for b in bloki: # отрисоувываем расположение каждого блока
        bloks(b[0],b[1],block_texture,screen)
pygame.init()
size = [900,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock() #Определение кол.во кадров в секунду
screen = pygame.display.set_mode(size)# Задаем размер окна
pygame.display.set_caption('DXBall')# Задаем имя игре
screen.fill(black) #заливаем фон черным цветом
path = os.path.dirname(__file__) #для картинок и музыки(это строчка нужна для редактора Atom)
#==================================================================
'''
    Загружаем музыку и картинки
'''
pygame.mixer.music.load(os.path.join(path, 'sound/main.mp3'))
lose_sound = pygame.mixer.Sound(os.path.join(path, 'sound/lose.wav'))
win_sound = pygame.mixer.Sound(os.path.join(path, 'sound/win.wav'))
pygame.mixer.music.play(-1)# включаем проигрывание фоновой музыки
#Картинки
win_img = pygame.image.load(os.path.join(path, 'img/win.jpg'))
lose_img = pygame.image.load(os.path.join(path, 'img/lose.jpg'))
player_texture = pygame.image.load(os.path.join(path, 'img/player_texture.png'))
ball_texture = pygame.image.load(os.path.join(path, 'img/ball_texture.png'))
block_texture = pygame.image.load(os.path.join(path, 'img/block_texture.png'))
ball_texture_activated = pygame.image.load(os.path.join(path, 'img/ball_texture_activated.png'))
bg = pygame.image.load(os.path.join(path, 'img/bg.jpg'))
start_screen = pygame.image.load(os.path.join(path, 'img/StartScreen.png'))
#==================================================================
'''
    Создание объектов на основе классов
'''
Ball = ball()
Ball.x = 350
Ball.y = 400
Ball.change_x = -2
Ball.change_y = -1
Ball.radius = 10
Player1 = player()
#==================================================================
'''
    Основные переменные для работы игры
'''
done = True
f1 = pygame.font.Font(os.path.join(path,'font/P.TTF'), 36)
bloki = []
raz = 6 # Количество раз, выполнения цыкла for (Для создания расплодения блоков)
bloky = 0 #Стандартное расположение блоков (Нужно для цыкла)
blokx = 0 #Стандартное расположение блоков (Нужно для цыкла)
win = 0 #Количество осков
motion = True #Нужно для того, чтобы после победы/проигрыша движение объектов прекратилось(оптимезация)
spis_x = [100,300,500,700]
wwin = False # Нужно для подсчета количество очков
'''
    Если бы мы расоположили эту переменную в главном цыкле и выполнилось бы условие (Шарика бы уничтожил блок),
    то вместо начисления 1 еденицы, было бы начисление как 2 еденицы
'''
lose = False #Если шарик упадет в низ, то будет конец игры
win_sound_play = True #Нужно для того, чтобы музыка проигралась один раз
lose_sound_play = True #Нужно для того, чтобы музыка проигралась один раз
ball_activated = True
for i in range(raz): #Создаем двоичный массив, в котором будет храниться расположение каждого блока
    for x in spis_x:
        bloky = bloky + 30
        if bloky == 210:
            bloky = 30
        bloki.append([x,bloky])
print(bloki)
start = False
while done:
    if start == False:
        screen.blit(start_screen,(0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                start = True
            elif i.key == pygame.K_l:
                lose = True
            elif i.key == pygame.K_w:
                win = 13
    if start:
        screen.blit(bg,(0,0))
        for b in bloki: # отрисоувываем расположение каждого блока
            bloks(b[0],b[1],block_texture,screen)
        # Поведение шарика при соприкосновении с платформой
        if abs(Ball.x > Player1.x - Player1.w) and abs(Ball.x < Player1.x + Player1.w) and abs(Ball.y > Player1.y-Player1.h) and abs(Ball.y < Player1.y+Player1.h):
            Ball.change_y = -1
            ball_activated = True
        # Управление платформой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Player1.x -= 3
        elif keys[pygame.K_RIGHT]:
            Player1.x +=3
        #Поведение блока при попадании на него шарика
        if ball_activated:
            for b in bloki:
                if abs(b[0] - Ball.x) < 100 and abs(b[1] - Ball.y) < 20:
                    bloki.remove(b)
                    wwin = True
                    ball_activated = False
                    Ball.change_y = 1
        else:
            pass
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
        text1 = f1.render('Number of points = '+ str(win), 1, (0, 0, 0))
        text2 = f1.render('Number of points = '+ str(win), 1, (255, 255, 255))
        #Поведение игры, если ты уничтожил все блоки
        if win >= 12:
            screen.blit(win_img,(0,0))
            pygame.mixer.music.pause() # Ставим паузу на музыку(фон)
            if win_sound_play:
                win_sound.play()
                win_sound_play = False
            motion = False
            screen.blit(text1, (170, 375))
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    play()
                    lose = False
                    start = False
        #Поведение игры, если ты уранил шарик
        if lose:
            screen.blit(lose_img,(0,0))
            pygame.mixer.music.pause()
            if lose_sound_play:
                lose_sound.play()
                lose_sound_play = False
            motion = False
            for b in bloki:
                bloki.remove(b)
            screen.blit(text2, (170, 375))
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    play()
                    lose = False
                    start = False
        if motion: #Прекращение отображения после победы
            #player_texture_draw(screen,Player1.x,Player1.y) #Выступают заместо хитбоксов
            ball_texture_draw(screen,Ball.x,Ball.y) #Выступают заместо хитбоксов
            Player1.draw(screen,player_texture)
            Ball.move()
        # здесь отводиться рендер шаего текста при победе/проигреше
        clock.tick(120)
    pygame.display.flip()
    print(Ball.y)
pygame.quit()
