import gym
from gym import spaces
import numpy as np
import pygame
import random
from .const import *
from .ball import GymBall


class Obstacle:
    def __init__(self, screen_width, ground_level, width, height, color):
        self.x = screen_width
        self.y = ground_level - height
        self.width = width
        self.height = height
        self.color = color

    def move(self, speed):
        self.x -= speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    

class JumpEnv(gym.Env):
    def __init__(self):
        super(JumpEnv, self).__init__()

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ball Jump Game")

        # Define action space: 0 - Do nothing, 1 - Jump
        self.action_space = spaces.Discrete(2)

        # Define observation space: RGB image of the screen
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(64, 64, 3), dtype=np.uint8
        )

        # Internal state
        self.ball = None
        self.obstacles = None
        self.obstacle_timer = None
        self.done = None
        self.clock = pygame.time.Clock()


    def reset(self):
        """Reset the environment to its initial state."""
        self.ball = GymBall(GROUND_LEVEL, BALL_RADIUS, JUMP_HEIGHT)
        self.obstacles = []
        self.obstacle_timer = 0
        self.done = False
        return self._get_observation()
    
    def step(self, action):
        """Take an action and return the new state, reward, done, and info."""
        if action == 1:  # Jump
            self.ball.jump()

        # Update the ball and obstacles
        self.ball.move()
        self._update_obstacles()

        # Check for collisions
        reward = 1
        if self._check_collision():
            self.done = True
            reward = -100  # Negative reward for collision
        
        # Return observation, reward, done flag, and info dictionary
        observation = self._get_observation()
        return observation, reward, self.done, {}
    

    def render(self, mode='human'):
        """Render the environment."""
        # Fill the screen with rich black color
        self.screen.fill(RICH_BLACK)

        # Draw the ground line
        pygame.draw.line(self.screen, NEON_BLUE, (0, GROUND_LEVEL), (SCREEN_WIDTH, GROUND_LEVEL), 2)

        # Draw the ball
        self.ball.draw(self.screen)

        # Draw the obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        # Update the display
        pygame.display.flip()

    
    def close(self):
        """Close the environment."""
        pygame.quit()

    def _get_observation(self):
        """Capture the screen and return it as an observation."""
        screen_array = pygame.surfarray.array3d(self.screen)
        obs = np.transpose(screen_array, (1, 0, 2))
        obs = pygame.surfarray.make_surface(obs)
        obs = pygame.transform.scale(obs, (64, 64))
        return pygame.surfarray.array3d(obs)

    
    def _check_collision(self):
        """Check for collisions between the ball and obstacles."""
        for obstacle in self.obstacles:
            if self.ball.get_rect().colliderect(obstacle.get_rect()):
                return True
        return False
    
    def _update_obstacles(self):
        """Update obstacles and generate new ones."""
        if self.obstacle_timer > 100:
            self.obstacles.append(Obstacle(SCREEN_WIDTH, GROUND_LEVEL, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, NEON_BLUE))
            self.obstacle_timer = 0

        # Move obstacles and remove those that have gone off-screen
        for obstacle in self.obstacles:
            obstacle.move(BALL_SPEED)
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.x + obstacle.width > 0]
        
        # Update obstacle timer
        self.obstacle_timer += 1