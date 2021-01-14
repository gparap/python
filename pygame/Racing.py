#gparap 12-11-2016
background_image_filename = 'assets/BG.jpg'
mouse_image_filename = 'assets/test.jpg'
car_red_image_path = 'assets/car_red.png'
car_blue_image_path = 'assets/car_red.png'  #82 x 123

import pygame
from colors import *
from pygame.locals import *
from sys import exit
import time

if (__name__ == "__main__"):
    #activate pygame lib
    pygame.init()

    #IMAGES
    background = pygame.image.load(background_image_filename)
    mouse_cursor = pygame.image.load(mouse_image_filename)   
    car_red = pygame.image.load(car_red_image_path)
    car_blue = pygame.image.load(car_blue_image_path)

    #SHAPES
    shape_rect = pygame.rect.Rect(10,20,200,300)

    #DISPLAY
    window_size = window_width, window_height = 640, 480
    window_screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
    pygame.display.set_caption("pygame racing proto")
    window_screen.fill(silver)

    #Text
    font = pygame.font.SysFont(None, 50, False, True)

    #FPS
    clock = pygame.time.Clock()
    frames_per_second = 60

    #CAR
    def car(x, y):
        window_screen.blit(car_red, (x, y))
    car_width = 82
    car_height = 123
    x = window_width / 2 - car_width / 2
    y = window_height - car_height
    x_velocity = 0

    #GAME LOOP     
    running = True
    while (running):

        #get all events loop
        for event in pygame.event.get():

            #quit
            if (event.type == pygame.QUIT):
                running = False
            
            #handle car movement
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    x_velocity -= 5
                elif (event.key == pygame.K_RIGHT):
                    x_velocity += 5
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    x_velocity = 0

        #------------------------------------------------------------------------------------
        #DRAW
        #------------------------------------------------------------------------------------
        #clear the screen to silver
        window_screen.fill(silver)
        
        #check boundaries
        x += x_velocity
        if (x < 0): 
            running = False
            message = font.render("out of bounds!", True, red)
            window_screen.blit(message, (100,100))
            time.sleep(0.5)
        if (x > window_width - 82): 
            running = False
            message = font.render("out of bounds!", True, red)
            window_screen.blit(message, (100,100))
            time.sleep(0.5)

        #draw the car
        car(x, y)

        #update
        clock.tick(frames_per_second)
        pygame.display.update()
        #------------------------------------------------------------------------------------
        #DRAW
        #------------------------------------------------------------------------------------

    #deactivate pygame lib
    pygame.quit()
    exit()