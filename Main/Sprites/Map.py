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
import Sprites.Player


# ---------------------------------------------------
# * Class
# ---------------------------------------------------
class Map(object):
    # -----------------------------------------------
    # * Instance Variables
    # -----------------------------------------------
    __num_tiles_horiz__ = 12
    __num_tiles_vert__ = 8
    __tile_patterns__ = [
                         [(0, 0, 0),       (255, 255, 255)],
                         [(255, 255, 255), (0, 0, 0)],
                         [(50, 25, 15),    (240, 210, 180)],
                         [(230, 230, 200), (75, 165, 75)],
                         [(227, 227, 227), (119, 119, 119)]
                        ]

    # -----------------------------------------------
    # * Object Initialization
    # -----------------------------------------------
    def __init__(self, graphics, map_num):
        self.graphics = graphics
        self.surface = graphics.screen
        self.pattern = Map.__tile_patterns__[map_num]
        self.tile_width = graphics.Width / Map.__num_tiles_horiz__
        self.tile_height = graphics.Height / Map.__num_tiles_vert__
        self.size = (self.tile_width, self.tile_height)
        self.player = Sprites.Player.Player(self.graphics)

    # -----------------------------------------------
    # * Display Update
    # -----------------------------------------------
    def update(self):
        # Draw the tiles.
        for ix in range(Map.__num_tiles_horiz__):
            for jy in range(Map.__num_tiles_vert__):
                rect = pygame.Rect((ix * self.tile_width,
                                    jy * self.tile_height),
                                   self.size)
                col = self.pattern[0]
                if((ix + jy) % 2 == 1):
                    col = self.pattern[1]

                pygame.draw.rect(self.surface,
                                 col,
                                 rect)
        # Draw the ring circles.
        rad = min(int(self.graphics.Height / 2),
                  int(self.graphics.Width / 2))
        x = int(self.graphics.Width / 2)
        y = int(self.graphics.Height / 2)
        pygame.draw.circle(self.surface,
                           (255, 255, 255),
                           (x, y),
                           rad)
        pygame.draw.circle(self.surface,
                           (0, 0, 0),
                           (x, y),
                           rad - 10)
        # Draw the starting lines.
        startline_line_size = (3, int(y * 2 / 3))
        rect = pygame.Rect((int(x * 5 / 6),
                            int(y * 2 / 3)),
                           startline_line_size)
        pygame.draw.rect(self.surface,
                         (185, 122, 87),
                         rect)
        rect = pygame.Rect((int(x * 7 / 6),
                            int(y * 2 / 3)),
                           startline_line_size)
        pygame.draw.rect(self.surface,
                         (185, 122, 87),
                         rect)
        # Draw the player
        self.player.update()
