#scree.py
import pygame
from .obstacle import Obstacle
from .bird import Bird
from .const import * 

class GameScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.background_color = BACKGROUND_COLOR
        self.bird = Bird(100, SCREEN_HEIGHT // 2)
        self.obstacles = []
        self.frame_count = 0

    def update(self):
        # Fill the screen with the background color
        self.screen.fill(self.background_color)

        # Move and draw the bird
        self.bird.move()
        self.bird.draw(self.screen)

        # Generate new pipes at a fixed frequency
        if self.frame_count % PIPE_SPAWN_FREQUENCY == 0:
            self.obstacles.append(Obstacle())

        # Move, draw, and check for off-screen pipes
        for obstacle in self.obstacles[:]:
            obstacle.move()
            obstacle.draw(self.screen)
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)

        self.frame_count += 1

    def check_collision(self):
        # Check for collisions between the bird and each pipe
        bird_rect = self.bird.get_rect()
        for obstacle in self.obstacles:
            top_rect, bottom_rect = obstacle.get_collision_rects()
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                return True
        return False

    def draw(self):
        pygame.display.flip()
