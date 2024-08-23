import pygame
import random
from const import *
from ball import Ball

# Initialize Pygame
pygame.init()



# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Jump Game")


class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = GROUND_LEVEL - OBSTACLE_HEIGHT
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.color = NEON_BLUE

    def move(self):
        self.x -= BALL_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


def check_collision(ball, obstacle):
    return ball.get_rect().colliderect(obstacle.get_rect())


def main():
    clock = pygame.time.Clock()
    ball = Ball()
    obstacles = []
    obstacle_timer = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball.jump()
            

        # Fill the screen with rich black color
        screen.fill(RICH_BLACK)

        # Draw the ground line
        pygame.draw.line(screen, NEON_BLUE, (0, GROUND_LEVEL), (SCREEN_WIDTH, GROUND_LEVEL), 2)

        # Move and draw the ball
        ball.move()
        ball.draw(screen)

        # Obstacle generation
        if obstacle_timer > 100:
            obstacles.append(Obstacle())
            obstacle_timer = 0

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw(screen)

        # Remove obstacles that have gone off the screen
        obstacles = [obstacle for obstacle in obstacles if obstacle.x + obstacle.width > 0]

        # Update obstacle timer
        obstacle_timer += 1

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()