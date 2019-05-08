import pygame
import random
import os

def animation_hero():
    global animCount #эти переменные должны быть глобальными, те берет инфу из основного кода
    global motion
    screen.blit(bg,(0,0)) #отображаем фон в первую очередь, чтобы прикрыть, то что мы намалевали в прошлый раз
    if animCount >=27: # если твой воторой кадр зайдет за отметку в 30 кадров, анимация начнеться с нуля
        '''
        У меня в списке(right_animation,left_animation) 9 картинок.
        Когда человек нажимает на левую кнопку, он берет список и грубо говоря повторяет один кадр 3 раз, после
        пересечения отметки в 3 раза, он пускает вторую картинку и так по порядку (1//3 = 0 , но 3//3 = 1)
        Таким образом мы берем за базовое значение количесто кадров 27, так как у нас 9 кадров, мы делим количество
        кадров в секундку(27) на количесвто кадров (9) = 3 раз один кадр (количество кадров в секунду / кол.картинок)
        Я взял 27 кадров/сек. так, как 30/9 = 3,333..., так что оптимальным решением будет взять 27 (27/9=3)
        '''
        animCount = 0
    if left:
        screen.blit(hero_left[animCount // 3],(x,y))
        animCount+=1
    elif right:
        screen.blit(hero_right[animCount // 3],(x,y))
        animCount+=1
    else:
        '''
        эта проверка нужна для того, чтобы поставить персонажа в правельную сторону
        если персонаж шел на лево, то и смотреть он будет в левую часть
        '''
        if motion == 1:
            screen.blit(hero_default_left,(x,y))
        else:
            screen.blit(hero_default_right,(x,y))
    pygame.display.flip()
pygame.init()
path = os.path.dirname(__file__)
pygame.mixer.music.load(os.path.join(path,'1.mp3')) #Загржает фоновую музыку
pygame.mixer.music.play() #включаем фоновую музыку (постоянная)
#pygame.mixer.music.play(-1) #зацикливание музыки
size = [800,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
path = os.path.dirname(__file__)
bg = pygame.image.load(os.path.join(path,'img/bg.jpg'))
##import img##
#right
#создаем списки с картинками
hero_right = [
    pygame.image.load(os.path.join(path,'img/hero/right/1.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/2.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/3.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/4.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/5.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/6.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/7.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/8.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/9.png'))
]
#left
hero_left = [
    pygame.image.load(os.path.join(path,'img/hero/left/1.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/2.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/3.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/4.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/5.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/6.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/7.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/8.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/9.png'))
]
hero_default_left = pygame.image.load(os.path.join(path,'img/hero/left/1.png'))
hero_default_right = pygame.image.load(os.path.join(path,'img/hero/right/1.png'))
wall = pygame.image.load(os.path.join(path,'img/pr.png'))
done = True
x = 20
y = 479
a_x = 500
a_y = 479
animCount = 0
left = False
right = False
motion = 0
JumpCount = 10
isJump = False
while done:
    screen.blit(bg,(0,0))
    screen.blit(hero_default_right,(x,y)) # стандартная позиция персонажа при запуске программы
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
        left = True
        right = False
        motion = 1 # определит куда будет смотреть персонаж при остановки (для функции animation_hero() )
    elif keys[pygame.K_RIGHT]:
        x += 3
        right = True
        left = False
        motion = 2 # определит куда будет смотреть персонаж при остановки (для функции animation_hero() )
    else:
        right = False
        left = False
        animCount = 0
    if not(isJump): #если не верно / if not true
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        '''
        Все базируется на параболе, дело в том , что стандартное значение JumpCount равно 10, а это значит что
        далее идет проверка, если число больше или равно -10, то оно будет подниматься по пораболе постипенно ( ( (i)**2 )/2 )
        ***( ( (i)**2 )/2 ) - в этом условии i будет равняться от 10 до -10, после чего переменная будет иметь число 10***
        таким образом она поднимется со стандартно уровня до отметки 1 и начнет снижаться до  стандартного уровня
        '''
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -=1
        else:
            isJump = False
            JumpCount = 10
    animation_hero()
    clock.tick(45)
    pygame.display.flip()
pygame.quit()
