import gym
from gym import spaces
import numpy as np
import pygame
from .screen import GameScreen
from .bird import Bird
from .obstacle import Obstacle
from .const import *

class FlappyBirdEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(FlappyBirdEnv, self).__init__()
        pygame.init()

        # Initialize game components
        self.screen = GameScreen()
        self.bird = self.screen.bird
        self.obstacles = self.screen.obstacles

        # Define action and observation spaces
        self.action_space = spaces.Discrete(2)  # 0: Do nothing, 1: Flap
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(SCREEN_WIDTH, SCREEN_HEIGHT, 3), dtype=np.uint8
        )

        self.clock = pygame.time.Clock()
        self.done = False
        self.score = 0

    def reset(self):
        # Reset game state
        self.screen = GameScreen()
        self.bird = self.screen.bird
        self.obstacles = self.screen.obstacles
        self.score = 0
        self.done = False
        return self._get_observation()

    def _get_observation(self):
        # Render the game and return the screen state
        self.screen.update()
        obs = pygame.surfarray.array3d(pygame.display.get_surface())
        return np.transpose(obs, (1, 0, 2))  # Transpose to (height, width, channels)

    def step(self, action):
        # Handle action: 0 for no action, 1 for flap
        if action == 1:
            self.bird.flap()

        # Update the screen (moves bird and pipes)
        self.screen.update()

        # Check for collision
        collision = self.screen.check_collision()

        # Set reward and check if game over
        if collision or not self.bird.alive:
            self.done = True
            reward = -100
        else:
            reward = 1  # Positive reward for staying alive

        # Increment score when passing through pipes
        for obstacle in self.obstacles:
            if obstacle.x + obstacle.width < self.bird.x and not obstacle.is_off_screen():
                self.score += 1
                reward += 10

        observation = self._get_observation()
        return observation, reward, self.done, {}

    def render(self, mode="human"):
        pygame.display.flip()
        self.clock.tick(30)

    def close(self):
        pygame.quit()
