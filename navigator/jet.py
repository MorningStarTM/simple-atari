import pygame
import math
from const import *


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center
    )
    win.blit(rotated_image, new_rect.topleft)

class Jet:
    def __init__(self, x, y):
        self.img = pygame.image.load(IMAGE)
        self.max_vel = 3
        self.vel = 0
        self.rotation_vel = 3
        self.angle = 0
        self.x, self.y = x, y
        self.acceration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win, offset_x, offset_y):
        # Adjust drawing based on the camera offset
        draw_x = self.x - offset_x
        draw_y = self.y - offset_y
        blit_rotate_center(win, self.img, (draw_x, draw_y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceration, -self.max_vel / 2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceration / 2, 0)
        self.move()

    def get_position(self):
        return self.x, self.y
