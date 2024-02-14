
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
import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from main import runner_pygame






difficuilty = None
time = None
cycles = None

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
playrectangle = pygame.Rect(300,350,200,40)
quitrectangle = pygame.Rect(300,height/2,200,40)

white = (255, 255, 255)
start = True

while True:  
      
    for ev in pygame.event.get():  
          
        if ev.type == pygame.QUIT:  
            pygame.quit()  
              
        if ev.type == pygame.MOUSEBUTTONDOWN:  

            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                pygame.quit()  
        

        if ev.type == pygame.MOUSEBUTTONDOWN and start == True:
            if 100 <= mouse[0] <= 500 and 350-40 <= mouse[1] <= 350+40:
                start = False
                playrectangle = pygame.Rect(300,350,0,0)
                text = smallfont.render('' , True , white)  
                text2 = smallfont.render('' , True , white)  
                quitrectangle = pygame.Rect(300,350,0,0)
                display.fill(white)
                load()


        

    # pygame.draw.rect(display, color, rectangle)

    mouse = pygame.mouse.get_pos()  
    # PLAY BUTTON
    if 100 <= mouse[0] <= 500 and 350-20 <= mouse[1] <= 350+20 and start == True:  
        pygame.draw.rect(display, color_light, playrectangle)
 
                
    else:  
        pygame.draw.rect(display, color_dark, playrectangle) 
    

    # QUIT BUTTON
    if 100 <= mouse[0] <= 500 and height/2-20 <= mouse[1] <= height/2+20 and start == True:  
        pygame.draw.rect(display, color_light, quitrectangle) 
                
    else:  
        pygame.draw.rect(display, color_dark, quitrectangle)
    

    display.blit(text, (350, height/2))  
    display.blit(text2, (350, 350))  




    pygame.display.update()  



    # runner_pygame()


    def load() -> None:

        screen = pygame.display.set_mode((800,800))
        screen.fill((250,240,230))
        

        slider1 = Slider(screen, 100, 100, 300, 40, min=0, max=4, step=1)
        slider2 = Slider(screen, 100, 300, 300, 40, min=0, max=100, step=1)
        slider3 = Slider(screen, 100, 500, 300, 40, min=0, max=5, step=1)
        output1 = TextBox(screen, 475, 100, 50, 50, fontSize=30)
        output2 = TextBox(screen, 475, 300, 75, 50, fontSize=30)
        output3 = TextBox(screen, 475, 500, 50, 50, fontSize=30)

        output1.disable()  # Act as label instead of textbox
        output2.disable()  # Act as label instead of textbox
        output3.disable()  # Act as label instead of textbox

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

            screen.fill((250,240,230))

            output1.setText(slider1.getValue())
            output2.setText(slider2.getValue())
            output3.setText(slider3.getValue())

            button = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            600,  # X-coordinate of top left corner
            700,  # Y-coordinate of top left corner
            150,  # Width
            75,  # Height

            # Optional Parameters
            text='Play',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(228,213,183),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: runner_pygame(slider1.getValue(), slider2.getValue(), slider3.getValue())  # Function to call when clicked on
            )

            button2 = Button(
        # Mandatory Parameters
            screen,  # Surface to place button on
            25,  # X-coordinate of top left corner
            10,  # Y-coordinate of top left corner
            225,  # Width
            75,  # Height

            # Optional Parameters
            text='difficuilty',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(217,185,155),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: print('Click')  # Function to call when clicked on
            )
            button3 = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            25,  # X-coordinate of top left corner
            200,  # Y-coordinate of top left corner
            150,  # Width
            75,  # Height

            # Optional Parameters
            text='time',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(217,185,155),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: print('Click')  # Function to call when clicked on
            )
                
            button4 = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            25,  # X-coordinate of top left corner
            400,  # Y-coordinate of top left corner
            150,  # Width
            75,  # Height

            # Optional Parameters
            text='cycles',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(217,185,155),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: print('Click')  # Function to call when clicked on
            )

            


    

            pygame_widgets.update(events)
            pygame.display.update()

 
