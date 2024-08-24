import pygame
import random
from const import SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (169, 169, 169)  # Gray color for asteroids
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self, speed):
        self.y += speed
        if self.y > SCREEN_HEIGHT:
            self.y = -self.size
            self.x = random.randint(0, SCREEN_WIDTH - self.size)

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)