import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
RICH_BLACK = (10, 10, 10)
NEON_BLUE = (0, 255, 255)
WHITE = (255, 255, 255)

# Game settings
FPS = 60
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
BALL_RADIUS = 20
BALL_COLOR = WHITE
BALL_SPEED = 5
JUMP_HEIGHT = 100

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Jump Game")


class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - OBSTACLE_HEIGHT
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.color = NEON_BLUE

    def move(self):
        self.x -= BALL_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
