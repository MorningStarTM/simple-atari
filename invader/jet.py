# jet.py
import pygame
from .bullet import Bullet
from .const import *

class Jet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Jet, self).__init__()
        self.image = pygame.image.load(JET).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))  # Adjust size as needed
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.last_shot_time = 0
        self.shoot_cooldown = 100  


    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self, bullet_group):
        # Get the current time
        current_time = pygame.time.get_ticks()

        # Check if enough time has passed since the last shot
        if current_time - self.last_shot_time > self.shoot_cooldown:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot_time = current_time  