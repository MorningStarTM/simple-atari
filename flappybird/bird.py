import pygame
from const import *

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BIRD_RADIUS
        self.color = BIRD_COLOR
        self.velocity = 0  # Initial vertical velocity
        self.alive = True

    def flap(self):
        # Apply an upward force when the bird flaps
        self.velocity = -FLAP_STRENGTH

    def move(self):
        # Apply gravity to the bird's vertical velocity
        self.velocity += GRAVITY
        self.y += self.velocity

        # Keep the bird within screen bounds
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > SCREEN_HEIGHT - self.radius:
            self.y = SCREEN_HEIGHT - self.radius
            self.alive = False  # Bird is dead if it hits the ground

    def draw(self, screen):
        # Draw the bird as a circle
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def get_rect(self):
        # Return the bird's bounding box for collision detection
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
