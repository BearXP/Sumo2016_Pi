# =========================================================
# ** MAP
# --------------------------------------------------------
# HISTORY:
#    Created By:   Mark Evans
#    Date Created: 4/Apr/2016
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
# * Class
# ---------------------------------------------------
class Map(object):
    # -----------------------------------------------
    # * Instance Variables
    # -----------------------------------------------

    # -----------------------------------------------
    # * Object Initialization
    # -----------------------------------------------
    def __init__(self, graphics, map_num):
        self.graphics = graphics
        self.surface = graphics.screen
        #self.pattern = Map.__patterns__[map_num]
        self.num_tiles_horiz = 8
        self.num_tiles_vert = 6
        self.tile_width = graphics.Width / self.num_tiles_horiz
        self.tile_height = graphics.Height / self.num_tiles_vert
        self.size = (self.tile_width, self.tile_height)

    # -----------------------------------------------
    # * Display Update
    # -----------------------------------------------
    def update(self):
        for ix in range(self.num_tiles_horiz):
            for jy in range(self.num_tiles_vert):
                rect = pygame.Rect((ix * self.tile_width,
                                    jy * self.tile_height),
                                   self.size)
                col = (0, 0, 0)
                if((ix + jy) % 2 == 1):
                    col = (255, 255, 255)

                pygame.draw.rect(self.surface,
                                 col,
                                 rect)
