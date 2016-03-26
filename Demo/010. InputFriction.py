import sys
import pygame
import numpy as np

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()

clock = pygame.time.Clock()

fps = 20
FRICTION = 10
GRAVITY = 0.5


class Character(object):
    def __init__(self, surface):
        self.surface = surface
        self.gravity = np.array([0.0, float(GRAVITY)])
        self.reset([screen_width / 2, screen_height / 2])

    def move_right(self):
        self.vel += np.array([1, 0])
        self.accel += np.array([1, 0])

    def move_left(self):
        self.vel += np.array([-1, 0])
        self.accel += np.array([-1, 0])

    def move_up(self):
        self.vel += np.array([0, -1])
        self.accel += np.array([0, -1])

    def move_down(self):
        self.vel += np.array([0, 1])
        self.accel += np.array([0, 1])

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move_up()
        if keys[pygame.K_a]:
            self.move_left()
        if keys[pygame.K_s]:
            self.move_down()
        if keys[pygame.K_d]:
            self.move_right()

        # Limit the X axis
        if self.pos[0] <= 0 or self.pos[0] >= screen_width:
            # Bounce off
            self.vel[0] *= -1
            self.accel[0] *= -1
            if self.pos[0] <= 0:
                self.pos[0] = 0
            elif self.pos[0] >= screen_width:
                self.pos[0] = screen_width
        # Limit the Y axis
        elif self.pos[1] <= 0 or self.pos[1] >= screen_height:
            self.vel[0] *= -1
            self.accel[0] *= -1
            if self.pos[1] <= 0:
                self.pos[1] = 0
            elif self.pos[1] >= screen_height:
                self.pos[1] = screen_height
        # Accel/Velocity if there aren't any limits
        else:
            self.vel = self.vel + (self.gravity + self.accel)
            if self.vel.dot(self.vel) < 1e-5:
                self.vel = np.zeros(2)
            # i.e. drops 10% each update
            self.accel *= (100 - FRICTION) / 100
            if self.accel.dot(self.accel) < 1e-5:
                self.accel = np.zeros(2)

        # Update position
        self.pos = self.pos + self.vel + 0.5 * self.gravity + self.accel

        # Debug
        print(self.pos, self.vel, self.accel)

        # Draw character
        self.character = pygame.Rect((self.pos[0], self.pos[1]), self.size)
        self.character.clamp_ip(screen_rect)

    def display(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.character)

    def reset(self, reset_position):
        self.accel = np.array([0, 0])
        self.vel = np.array([0.0, 0.0])
        self.pos = np.array(reset_position)
        self.size = (10, 10)


def main():
    player1 = Character(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player1.reset(pygame.mouse.get_pos())

        player1.move()

        screen.fill((0, 0, 0))

        player1.display()

        pygame.display.update(screen_rect)
        clock.tick(fps)

if __name__ == "__main__":
    main()
