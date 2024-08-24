import pygame
from obstacle import Asteroid
import random
from const import *

class GameScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jet and Asteroids")
        self.background_color = BACKGROUND_COLOR

        self.asteroids = [
            Asteroid(
                random.randint(0, SCREEN_WIDTH - ASTEROID_MAX_SIZE),
                random.randint(-SCREEN_HEIGHT, 0),
                random.randint(ASTEROID_MIN_SIZE, ASTEROID_MAX_SIZE)
            ) for _ in range(ASTEROID_COUNT)
        ]

    def update(self):
        self.screen.fill(self.background_color)
        for asteroid in self.asteroids:
            asteroid.move(ASTEROID_SPEED)
            asteroid.draw(self.screen)

    def check_collision(self, player_rect):
        for asteroid in self.asteroids:
            if player_rect.colliderect(asteroid.rect):
                return True
        return False


