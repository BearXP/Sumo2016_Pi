
# Import a library of functions called 'pygame'
import pygame
import Graphics
import Input

# Initialize the game engine
Graphics.init(480, 320)
Input.init()

# Loop until the user clicks the close button.
done = False
loopCount = 0

# Loop as long as done == False
while not done:
    loopCount += 1
    Input.update()
    if(Input.Trigger(Input.Close)):
        done = True
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    if((int(loopCount / 15) % 2) == 1):
        Graphics.screen.fill(Graphics.GREEN)
    else:
        Graphics.screen.fill(Graphics.RED)
    Graphics.update()


# Close window and exit
pygame.quit()
