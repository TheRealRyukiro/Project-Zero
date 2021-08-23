import pygame


#-------Game initialization---------#
# initializes the pygame and starts the game 
pygame.init()




#----------Screen initialization-------------#

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) # creates the screen and set the (width , height) of the GUI

#----------Title and logo --------------------#
pygame.display.set_caption("Text Adventure v0.0.1")  #creates and set the caption tile for the game 
icon = pygame.image.load("GUI-Version/gameicon.png")            # loads the image fo the game called gameicon   
pygame.display.set_icon(icon)                         # displays the icon next the caption tile in the GUI

#----------------Game loop-----------------#
running = True  # variable create to tell pygame whether its runnning or not 
while running:
    for event in pygame.event.get():        # events in pygame or anything that can be interacted with examples include button presses mouse clicks 
        if event.type == pygame.QUIT:      # while the game is runningg the program checks to see if the quit event button has been pressed
            running = False                     # when the quit event button is pressed the while loop stops and the game is closed