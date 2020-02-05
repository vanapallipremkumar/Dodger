import pygame, sys
from pygame.locals import *
import ctypes
user=ctypes.windll.user32
width,height=user.GetSystemMetrics(0),user.GetSystemMetrics(1)
 
pygame.init()
 
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
 
clock = pygame.time.Clock()

blue=pygame.transform.scale(pygame.image.load("cloud.png").convert_alpha(),(width,height))
black=pygame.transform.scale(pygame.image.load("cloud.png").convert_alpha(),(width,height))
 
x = 0
y = height
 
while True:
    screen.fill((30,191,255))
    screen.blit(blue, (0,x))
    screen.blit(black, (0,y))
    pygame.display.update()
    x += 5
    y += 5
 
    if x >= height:
        x = -1*(height-y)
    if y >= height:
        y = -1*(height-x)
 
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
