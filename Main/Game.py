
# Import a library of functions called 'pygame'
import pygame
import Input
import random
 
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the height and width of the screen
size = (480, 320)
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sumobot")
Input.init()

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    Input.update()
    if( Input.Trigger( Input.Close ) ):
        done = True
            
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(30)


# Close window and exit
pygame.quit()
    




# Be IDLE friendly
pygame.quit()
