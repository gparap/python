#gparap 29-10-2016
import pygame
from time import sleep
pygame.init()
##########################################################################
# Vars
##########################################################################
helper_movement = "V for vertical |or| H for horizontal movement only"
is_game_over = False
#Colors
color_white = (255,255,255)
color_black = (0,0,0)
color_red = (255,0,0)
color_green = (0,255,0)
#Game window
game_title = 'snake'
screen_width = 640
screen_height = 480
game_window = pygame.display.set_mode([screen_width, screen_height]); 
pygame.display.set_caption(game_title)
#Snake
snake_block_width = 10
snake_block_height = 10
head_x = screen_height/2 #snake head position x
head_y = screen_height/2 #snake head position x
tail_x = screen_height/2 #snake tail position y
tail_y = screen_height/2 #snake tail position y
speed = 5
velocity_x = 0
velocity_y = 0
#Clock
clock = pygame.time.Clock()
fps = 60
#Text
font = pygame.font.SysFont(None, 50)
##########################################################################
# Functions
##########################################################################
def fDisplayMessage(messageText, messageColor):
    display_message = font.render(messageText, True, messageColor)
    game_window.blit(display_message, [screen_width/2, screen_height/2])
##########################################################################
# Game Loop
##########################################################################
while (is_game_over != True):
    #get all events                     
    for event in pygame.event.get():
        #exit loop
        if (event.type == pygame.QUIT): 
            is_game_over = True
        #arrow keys pressed
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                velocity_x = -1
                speed = 5
                helper_movement = "H" 
            elif (event.key == pygame.K_RIGHT):
                velocity_x = 1
                speed = 5
                helper_movement = "H"
            elif (event.key == pygame.K_UP):
                velocity_y = -1
                speed = 5
                helper_movement = "V"
            elif (event.key == pygame.K_DOWN):
                velocity_y = 1
                speed = 5
                helper_movement = "V"
        #arrow keys released        
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or
                event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                speed = 0
            
    #move the snake
    if (helper_movement == "H"):
        head_x += speed * velocity_x
    elif (helper_movement == "V"):
        head_y += speed * velocity_y

    #check boundaries to game over
    if ((head_x > screen_width - snake_block_width) or (head_x < 0) or
        (head_y > screen_height - snake_block_width) or (head_y < 0)):      
        is_game_over = True
         
    #clear screen to white
    game_window.fill(color_white)
    
    #rectangles
    pygame.draw.rect(game_window, color_red, [head_x, head_y, snake_block_width, snake_block_height])
    game_window.fill(colorGreen, rect=[i,100,20,20])

    #update and draw
    clock.tick(fps)
    pygame.display.update()   

#messages to players
fDisplayMessage("Game Over Man!", color_red)
pygame.display.update()
sleep(1.5)

#quit    
pygame.quit()
quit()
