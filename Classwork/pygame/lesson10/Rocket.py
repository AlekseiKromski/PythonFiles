import pygame
pygame.init()
WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Rocket:
    # ширина и высота у всех
    # экземпляров-ракет будут одинаковы
    width_rocket = 50
    height_rocket = 20
    def __init__(self, surface, color,j):
        """Конструктору необходимо передать поверхность, по которой
        будет летать ракета и цвет самой ракеты"""
        self.surf = surface
        self.color = color
        # Методы поверхности get_width() и get_height() возвращают ее
        # размеры.
        # Координаты верхнего левого угла ракеты устанавливаются так,
        # чтобы ракета летела ровно по центру поверхности по горизонтали
        # и появлялась снизу.
        if j == 1:
            self.x = 0
            self.y = surface.get_height()//2 - Rocket.width_rocket//2
        else:
            self.x = surface.get_width()
            self.y = surface.get_height()//2 - Rocket.width_rocket//2
    def fly(self,j):
        """Вызов метода fly() поднимает ракету на 3 пикселя.
        Если ракета скрывается вверху, она снова появится снизу"""
        #pygame.draw.polygon(self.surf, self.color, ([100,100], [50,200],[150,200]))
        pygame.draw.rect(self.surf, self.color, (self.x, self.y,Rocket.width_rocket, Rocket.height_rocket))
        if j == 1:
            self.x += 5
            if self.x > WIN_WIDTH:
                self.x = 0
        else:
            self.x -= 8
            if self.x < -Rocket.width_rocket:
                # Поэтому перебрасываем ракету под нижнюю границу окна.
                self.x = WIN_WIDTH
        # Если координата y ракеты уходит за -50, то значит она
        # полностью скрылась вверху.

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# левая белая поверхность, равная половине окна
surf_left = pygame.Surface((WIN_WIDTH, WIN_HEIGHT//2))
surf_left.fill(WHITE)
# правая черная поверхность, равная другой половине окна
surf_right = pygame.Surface((WIN_WIDTH, WIN_HEIGHT//2))
# размещаем поверхности на главной, указывая координаты
# их верхних левых углов
sc.blit(surf_left, (0, 0))
sc.blit(surf_right, (0, WIN_HEIGHT//2))
# создаем черную ракету для левой поверхности
# и белую - для правой
j = 0
rocket_left = Rocket(surf_left, BLACK,j)
rocket_right = Rocket(surf_right, WHITE,j)
# какая половина активна, до первого клика - никакая
active_left = False
active_right = False
done = True

while done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.MOUSEBUTTONUP:
        # если координата X клика меньше половины окна,
        # т. е. клик произошел в левой половине ...
            if i.pos[1] < WIN_HEIGHT//2:
                # то активируем левую, отключаем правую
                active_left = True
                active_right = False
            elif i.pos[1] > WIN_HEIGHT//2: # pos = [x,y] , x - 0  y - 1
                # иначе - наоборот
                active_right = True
                active_left = False
    if active_left:
        # Если активна левая поверхность,
        # то заливаем только ее цветом,
        surf_left.fill(WHITE)
        # поднимаем ракету,
        j = 1
        rocket_left.fly(j)
        # заново отрисовываем левую поверхность на главной.
        sc.blit(surf_left, (0, 0))
    elif active_right:
        j = 0
        # Если активна правая -> аналогично
        surf_right.fill(BLACK)
        rocket_right.fly(j)
        sc.blit(surf_right, (0, WIN_HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(20)
pygame.quit()
