
# Import a library of functions called 'pygame'
import Graphics
import Input
 
# Initialize the game engine
Graphics.init(480, 320)
Input.init()

# Loop until the user clicks the close button.
done = False
 
# Loop as long as done == False
while not done:
 
    Input.update()
    if( Input.Trigger( Input.Close ) ):
        done = True
            
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    Graphics.update()


# Close window and exit
pygame.quit()
    
