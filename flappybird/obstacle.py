import pygame
import random
from const import *

class Obstacle:
    def __init__(self):
        self.width = PIPE_WIDTH
        self.color = PIPE_COLOR
        self.gap = PIPE_GAP
        self.speed = PIPE_SPEED

        # Initial positions of the pipes
        self.x = SCREEN_WIDTH
        self.top_height = random.randint(50, SCREEN_HEIGHT // 2)
        self.bottom_height = SCREEN_HEIGHT - self.top_height - self.gap

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        # Draw the top pipe
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.top_height))
        # Draw the bottom pipe
        pygame.draw.rect(screen, self.color, (self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height))

    def is_off_screen(self):
        # Check if the pipe is off the left side of the screen
        return self.x + self.width < 0

    def get_collision_rects(self):
        # Returns the rects for collision detection
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pygame.Rect(self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height)
        return top_rect, bottom_rect
