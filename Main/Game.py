# Import a library of functions called 'pygame'
import sys
import pygame

import Graphics
import Input
import Sprites.Map

# Initialize the game engine
screen_width = 480
screen_height = 320
Graphics.init(screen_width, screen_height)
Input.init()
map = Sprites.Map.Map(Graphics, 1)


def main():
    # Loop until the user clicks the close button.
    done = False
    loopCount = 0
    while not done:
        loopCount += 1
        Input.update()
        if(Input.Trigger(Input.Close)):
            done = True
        map.update()
        Graphics.update()


# Close window and exit
pygame.quit()
sys.exit()

if __name__ == "__main__":
    main()
