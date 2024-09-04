# bullet.py
import pygame
from .const import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.image.load(BULLET).convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 8))  # Adjust size as needed
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -8

    def update(self):
        self.rect.y += self.speed
        # Remove bullet if it goes off screen
        if self.rect.bottom < 0:
            self.kill()
