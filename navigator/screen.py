import pygame
from obstacle import Asteroid
import random
from const import *
import math
from noise import pnoise1
from scipy.interpolate import interp1d
import numpy as np

def generate_dynamic_path(screen_width, screen_height, num_points=10, path_width=200, noise_scale=0.1):
    # Generate random control points using Perlin noise
    control_points = []
    for i in range(num_points):
        x = i * (screen_height // num_points)
        noise_val = pnoise1(i * noise_scale)  # Perlin noise value
        y = int((screen_width // 2) + noise_val * (screen_width // 3))
        control_points.append((y, x))
    
    # Generate Bézier curve from control points
    curve_points = generate_bezier_curve(control_points, n_points=500)

    # Define the left and right boundaries of the path
    left_boundary = [(x - path_width // 2, y) for x, y in curve_points]
    right_boundary = [(x + path_width // 2, y) for x, y in curve_points]

    return left_boundary, right_boundary, curve_points


def generate_bezier_curve(control_points, n_points=100):
    """Generate a Bézier curve from control points."""
    n = len(control_points) - 1
    t = np.linspace(0.0, 1.0, n_points)
    curve = np.zeros((n_points, 2))
    for i, (x, y) in enumerate(control_points):
        binomial_coeff = np.math.comb(n, i)
        bernstein_poly = binomial_coeff * (t ** i) * ((1 - t) ** (n - i))
        curve[:, 0] += x * bernstein_poly
        curve[:, 1] += y * bernstein_poly
    return curve


class GameScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jet and Asteroids")
        self.background_color = BACKGROUND_COLOR

        self.asteroids = [
            Asteroid(
                random.randint(0, SCREEN_WIDTH),
                random.randint(-SCREEN_HEIGHT, 0),
                random.choice(ASTEROID_IMAGES)
            ) for _ in range(ASTEROID_COUNT)
        ]

    def update(self, offset_x, offset_y):
        self.screen.fill(self.background_color)
        for asteroid in self.asteroids:
            asteroid.move(0)  # Asteroids don't move vertically; they are static in relation to the player
            asteroid.draw(self.screen, offset_x, offset_y)

    def check_collision(self, player_rect):
        for asteroid in self.asteroids:
            if player_rect.colliderect(asteroid.rect):
                return True
        return False
    


class DynamicGameScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jet and Asteroids")
        self.background_color = BACKGROUND_COLOR

        # Generate dynamic path
        self.left_boundary, self.right_boundary, self.path_points = generate_dynamic_path(SCREEN_WIDTH, SCREEN_HEIGHT)

        # List to hold asteroid objects
        self.asteroids = []
        self.generate_asteroids()

    def generate_asteroids(self):
        self.asteroids.clear()
        for _ in range(ASTEROID_COUNT):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(-SCREEN_HEIGHT*4, 0)
            
            # Ensure asteroids are not placed directly on the path
            if not self.is_on_path(x, y):
                self.asteroids.append(Asteroid(x, y, random.choice(ASTEROID_IMAGES)))

    def is_on_path(self, x, y):
        # Check if a point (x, y) is within the path boundaries
        for (left_x, left_y), (right_x, right_y) in zip(self.left_boundary, self.right_boundary):
            if left_y <= y <= right_y and left_x <= x <= right_x:
                return True
        return False

    def update(self, offset_x, offset_y):
        self.screen.fill(self.background_color)

        for asteroid in self.asteroids:
            asteroid.move(0)  # Asteroids are static in relation to the player
            asteroid.draw(self.screen, offset_x, offset_y)

    def check_collision(self, player_rect):
        for asteroid in self.asteroids:
            if player_rect.colliderect(asteroid.rect):
                return True
        return False


