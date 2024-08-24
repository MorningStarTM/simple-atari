import pygame
import random
from const import SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, speed):
        self.y += speed
        if self.y > SCREEN_HEIGHT:
            self.y = -self.rect.height
            self.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen, offset_x, offset_y):
        screen.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))