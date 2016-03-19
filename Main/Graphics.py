# =========================================================
# ** GRAPHICS
# --------------------------------------------------------
# HISTORY:
#    Created By:   Mark Evans
#    Date Created: 16/Mar/2016
# DESCRIPTION:
#    Handles graphics setup & update.
# INTERFACE:
#    import Graphics
#    Graphics.init(width, height)
#    while(1):
#        Graphics.update()
# =========================================================

# ---------------------------------------------------
# * Libraries
# ---------------------------------------------------
import pygame

# ---------------------------------------------------
# * Public Constants
# ---------------------------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = None
screen = None


# ---------------------------------------------------
# * Object Initialization
# ---------------------------------------------------
def init(width, height, fullscreen=False):
    global screen, clock
    pygame.init()
    size = (width, height)
    if fullscreen:
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sumobot")
    clock = pygame.time.Clock()


# ---------------------------------------------------
# * Frame Update
# ---------------------------------------------------
def update():
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(15)
