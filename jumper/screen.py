import pygame
import random
from const import *
from ball import Ball
import numpy as np

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
        self.speed = 5

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


def check_collision(ball, obstacle):
    return ball.get_rect().colliderect(obstacle.get_rect())

def get_screen_observation():
    screen_array = pygame.surfarray.array3d(screen)
    screen_array = np.transpose(screen_array, (1, 0, 2))  # Convert from (width, height, color) to (height, width, color)
    return screen_array


def save_observation(observation, filename="observation.npy"):
    """
    Saves the given observation as a NumPy array file.

    Parameters:
    - observation: The NumPy array containing the observation to save.
    - filename: The name of the file to save the observation to. Defaults to "observation.npy".
    """
    np.save(filename, observation)
    print(f"Observation saved to {filename}")



def main():
    clock = pygame.time.Clock()
    ball = Ball()
    obstacles = []
    obstacle_timer = 0
    frame = 0

    running = True
    while running:
        frame += 1
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

        # Check for collision with ball
            if check_collision(ball, obstacle):
                running = False  # End the game if collision occurs


        # Remove obstacles that have gone off the screen
        obstacles = [obstacle for obstacle in obstacles if obstacle.x + obstacle.width > 0]

        # Update obstacle timer
        obstacle_timer += 1

        
        # Capture the screen as an observation
        observation = get_screen_observation()
        
        # Print shape of observation to verify (optional)
        #save_observation(observation)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()