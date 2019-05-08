import os
import pygame
class Sprite:
      def __init__(self, xpos, ypos, filename):
         self.x = xpos
         self.y = ypos
         self.bitmap = image.load(filename)
         self.bitmap.set_colorkey((0,0,0))
      def set_position(self, xpos, ypos):
         self.x = xpos
         self.y = ypos
      def render(self):
         screen.blit(self.bitmap, (self.x, self.y))
 #wad
path = os.path.dirname(__file__)
pygame.init()
size = [640,480]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
path = os.path.dirname(__file__)
bg = bg = pygame.image.load(os.path.join(path,'img/bg.bmp'))
done = True
while done:
    screen.blit(bg,(0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    clock.tick(45)
    pygame.display.flip()
pygame.quit()
