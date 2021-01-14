#gparap 10-11-2016
#ASSETS
background_image_filename = 'assets/BG.jpg'
mouse_image_filename = 'assets/test.jpg'
bullet_image_filename = 'assets/bullet_blue.png'

import pygame
from colors import *
from pygame.locals import *
from sys import exit
from classes import CBaseSprite as sprite_base

#activate pygame lib
pygame.init()

#IMAGES
background = pygame.image.load(background_image_filename)
mouse_cursor = pygame.image.load(mouse_image_filename)
bullet = pygame.image.load(bullet_image_filename)

#SHAPES
shape_rect = pygame.rect.Rect(10,20,200,300)

#DISPLAY
window_size = window_width, window_height = 640, 480
window_screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("protoMouse")
window_screen.fill(silver)

#FPS
clock = pygame.time.Clock()
frames_per_second = 60

#GAME LOOP     
running = True
while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        
    #DRAW--------------------------------------------------------------------------------
    window_screen.blit(background, (0,0))               #background
    x, y = pygame.mouse.get_pos()
    window_screen.blit(mouse_cursor, (x,y))             #mouse-moving image
    pygame.draw.rect(window_screen, aqua, shape_rect)   #rectangle
    pixelArray = pygame.PixelArray(window_screen)       #make an array of pixels
    pixelArray[200][205] = black                        	#using the window surface
    pixelArray[205][200] = black                            #in order to manipulate
    pixelArray[210][205] = black                            #some of these pixels
    pixelArray[215][200] = black
    pixelArray[220][205] = black
    del pixelArray                                      #unlock the surface
    window_screen.blit(bullet.image, (50,50));          #bullets
    window_screen.blit(bullet.image, (70,50));
    window_screen.blit(bullet.image, (90,50));
    window_screen.blit(bullet.image, (50,70));
    window_screen.blit(bullet.image, (70,70));
    window_screen.blit(bullet.image, (90,70));
    window_screen.blit(bullet.image, (50,90));
    window_screen.blit(bullet.image, (70,90));
    window_screen.blit(bullet.image, (90,90));

    clock.tick(frames_per_second)                       #control updating to 60 fps
    pygame.display.update();
    #DRAW--------------------------------------------------------------------------------

#deactivate pygame lib
pygame.quit()
exit()