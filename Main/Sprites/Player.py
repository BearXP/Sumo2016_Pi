import Input
import pygame
import math


class Player(object):
    __robotSizeFromScreen__ = 0.06

    # -----------------------------------------------
    # * Object Initialization
    # -----------------------------------------------
    def __init__(self, graphics):
        # Setup input
        self.input = input
        # Setup robot size
        self.graphics = graphics
        self.surface = graphics.screen
        minScreenDim = min(graphics.Width, graphics.Height)
        self.char_width = minScreenDim * Player.__robotSizeFromScreen__
        self.char_height = minScreenDim * Player.__robotSizeFromScreen__
        self.size = (self.char_width, self.char_height)
        # Setup robot kinematics
        self.pos = [graphics.Width / 4, graphics.Height / 2, 0]  # X, Y, Theta
        self.vel = [0, 0, 0]                                     # X, Y, Theta
        self.acc = [0, 0, 0]                                     # X, Y, Theta

    # -----------------------------------------------
    # * Frame Update
    # -----------------------------------------------
    def update(self):
        # Inputs
        self.update_kinematics()
        # Draw
        rect = pygame.Rect((self.pos[0] - self.size[0] / 2,
                            self.pos[1] - self.size[1] / 2),
                           self.size)
        pygame.draw.rect(self.surface,
                         (255, 0, 0),
                         rect)

    # -----------------------------------------------
    # * Update Kinematics
    # -----------------------------------------------
    def update_kinematics(self):
        # Front/back
        if(Input.Hold(Input.Up)):
            self.acc[0] = 100
            self.acc[1] = 100
        elif(Input.Hold(Input.Down)):
            self.acc[0] = -100
            self.acc[1] = -100
        else:
            self.acc[0] = -self.vel[0] / 20
            self.acc[1] = -self.vel[1] / 20
        # Left.right
        if(Input.Hold(Input.Left)):
            self.acc[2] = -5
        elif(Input.Hold(Input.Right)):
            self.acc[2] = 5
        else:
            self.acc[2] = 0
        # Velocity
        self.vel[0] += self.acc[0] * 0.1
        self.vel[1] += self.acc[1] * 0.1
        self.vel[2] += self.acc[2] * 0.1
        # Resistance
        for i in range(0, 2, 1):
            self.vel[i] *= 0.90
            if(abs(self.vel[i]) < 0.3):
                self.vel[i] = 0
        # Position
        self.pos[0] += self.vel[0] * 0.1 * math.cos(self.pos[2])
        self.pos[1] += self.vel[1] * 0.1 * math.sin(self.pos[2])
        self.pos[2] += self.vel[2] * 0.1
        self.pos[2] *= 0.90
        if(abs(self.pos[2]) < 0.3):
            self.pos[2] = 0
