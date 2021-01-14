#gparap 10-11-2016
#import pygame and whatever module necessary
import pygame, sys

#placeholder file for color definitions
from colors import *    

#initialize pygame modules
pygame.init()

#set up the display surfaces (aka Screen)
game_SIZE = WIDTH, HEIGHT = 640, 480
pygame.display.set_caption("protoKeys")
surface_SCREEN = pygame.display.set_mode(game_SIZE)
surface_ALPHA = surface_SCREEN.convert_alpha() #transparent surface

#draw to the surface
surface_SCREEN.fill(WHITE)
pygame.draw.polygon(surface_SCREEN, GRAY, ((0,0), (0,100), (100,100), (100,0)), 1)
pygame.draw.line(surface_SCREEN, BLACK,(100,100),(150,150),1)
pygame.draw.line(surface_SCREEN, BLACK,(270,290),(370,300),1)

#access the pixels of the (locked) surface for precise drawing
pixelObject = pygame.PixelArray(surface_SCREEN)
pixelObject[0][0] = RED
pixelObject[1][1] = GREEN
pixelObject[2][2] = BLUE
del pixelObject

#Fonts
FONT = pygame.font.SysFont("Times New Roman", 20)
surface_TEXT = FONT.render("Testing fonts", 0, RED)
text_positionXY = (100,100)

#Images
image_cat = pygame.image.load("assets\cat.png")
image_cat_positionX = 0
image_cat_positionY = 0

#frame rate
FPS = 60
CLOCK = pygame.time.Clock()

################################################################################################
#GAME LOOP
################################################################################################
while True:
    #clear the screen
    screen.fill(white)

    #blit the text to the screen surface
    surface_SCREEN.blit(surface_TEXT, text_positionXY)

    #loop through the events queue
    for event in pygame.event.get():
        #quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #move the image with arrows
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_LEFT:
                image_cat_positionX -= 10
            if event.key == pygame.K_RIGHT:
                image_cat_positionX += 10
            if event.key == pygame.K_UP:
                image_cat_positionY -= 10
            if event.key == pygame.K_DOWN:
                image_cat_positionY += 10

    #update the "..." image position X
    image_cat_positionX += 1
    if image_cat_positionX == 300:
        image_cat_positionX = 0

    #blit the image to the screen surface
    surface_SCREEN.blit(image_cat, (image_cat_positionX,image_cat_positionY))

    #display the screen surface
    pygame.display.update()

    #control the frame rate
    CLOCK.tick(FPS)