# asteroid.py
import pygame
import random
from .const import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load(ASTEROID).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Scale as needed
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(1, 4)

    def update(self):
        # Move asteroid down the screen
        self.rect.y += self.speed
        # Remove asteroid if it goes off screen
        if self.rect.top > HEIGHT:
            self.kill()