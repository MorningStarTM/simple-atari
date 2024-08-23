import pygame
from const import *

class Ball:
    def __init__(self):
        self.x = 100
        self.y = GROUND_LEVEL - BALL_RADIUS
        self.dy = 0
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.dy = -JUMP_HEIGHT
            self.on_ground = False

    def move(self):
        self.dy += 3.5  # Gravity effect
        self.y += self.dy

        # Ball hits the ground
        if self.y >= GROUND_LEVEL - BALL_RADIUS:
            self.y = GROUND_LEVEL - BALL_RADIUS
            self.dy = 0
            self.on_ground = True

    def draw(self, screen):
        pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), BALL_RADIUS)

    def get_rect(self):
        return pygame.Rect(self.x - BALL_RADIUS, self.y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
