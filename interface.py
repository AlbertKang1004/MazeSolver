
# $$\      $$\
# $$$\    $$$ |
# $$$$\  $$$$ | $$$$$$\  $$$$$$$$\  $$$$$$\
# $$\$$\$$ $$ | \____$$\ \____$$  |$$  __$$\
# $$ \$$$  $$ | $$$$$$$ |  $$$$ _/ $$$$$$$$ |
# $$ |\$  /$$ |$$  __$$ | $$  _/   $$   ____|
# $$ | \_/ $$ |\$$$$$$$ |$$$$$$$$\ \$$$$$$$\
# \__|     \__| \_______|\________| \_______|
#  $$$$$$\            $$\
# $$  __$$\           $$ |
# $$ /  \__| $$$$$$\  $$ |$$\    $$\  $$$$$$\   $$$$$$\
# \$$$$$$\  $$  __$$\ $$ |\$$\  $$  |$$  __$$\ $$  __$$\
#  \____$$\ $$ /  $$ |$$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
# $$\   $$ |$$ |  $$ |$$ |  \$$$  /  $$   ____|$$ |
# \$$$$$$  |\$$$$$$  |$$ |   \$  /   \$$$$$$$\ $$ |
#  \______/  \______/ \__|    \_/     \_______|\__|
#
#     _       __            ____              
#    (_)___  / /____  _____/ __/___ _________ 
#   / / __ \/ __/ _ \/ ___/ /_/ __ `/ ___/ _ \
#  / / / / / /_/  __/ /  / __/ /_/ / /__/  __/
# /_/_/ /_/\__/\___/_/  /_/  \__,_/\___/\___/


from maze import Maze
from game import MazeGame
import pygame
import sys

# initialize the pygame window, this is the main menu that users will use to interact and set levels to the game.
pygame.init()


resolution = (800, 800)

display = pygame.display.set_mode(resolution)

color = (222, 222, 222)

# light shade of the button  
color_light = (170,170,170)  
  
# dark shade of the button  
color_dark = (100,100,100)  

width = display.get_width()
height = display.get_height()

smallfont = pygame.font.SysFont('Times New Roman',35)  
text = smallfont.render('QUIT?' , True , color)  
text2 = smallfont.render('PLAY?' , True , color)  

while True:  
      
    for ev in pygame.event.get():  
          
        if ev.type == pygame.QUIT:  
            pygame.quit()  
              
        if ev.type == pygame.MOUSEBUTTONDOWN:  

            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                pygame.quit()  

        

    mouse = pygame.mouse.get_pos()  
    
    # PLAY BUTTON
    if 100 <= mouse[0] <= 500 and 350-40 <= mouse[1] <= 350+40:  
        pygame.draw.rect(display,color_light,[300,350,200,40])  
                
    else:  
        pygame.draw.rect(display,color_dark,[300,350,200,40])  
    

    # QUIT BUTTON
    if 100 <= mouse[0] <= 500 and height/2-40 <= mouse[1] <= height/2+40:  
        pygame.draw.rect(display,color_light,[300,height/2,200,40])  
                
    else:  
        pygame.draw.rect(display,color_dark,[300,height/2,200,40])  
    

    display.blit(text, (350, height/2))  
    display.blit(text2, (350, 350))  


    # pygame.draw.rect(display, color_dark, pygame.Rect(30, 30, 60, 60), 10)
    # rect = pygame.rect(50, 50, 50, 50)
    # pygame.draw.rect(display, (0, 0, 128), rect)
    # display.blit(text, (350, height/2))  


    pygame.display.update()  