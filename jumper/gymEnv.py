import gym
from gym import spaces
import numpy as np
import pygame
import random
from const import *
from ball import Ball
from screen import Obstacle

class JumpEnv(gym.Env):
    def __init__(self):
        super(JumpEnv, self).__init__()

        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Ball Jump Game")

        # Define action space: 0 - Do nothing, 1 - Jump
        self.action_space = spaces.Discrete(2)

        # Define observation space: RGB image of the screen
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(self.SCREEN_HEIGHT, self.SCREEN_WIDTH, 3), dtype=np.uint8
        )

        # Internal state
        self.ball = None
        self.obstacles = None
        self.obstacle_timer = None
        self.done = None
        self.clock = pygame.time.Clock()


    def reset(self):
        """Reset the environment to its initial state."""
        self.ball = Ball(GROUND_LEVEL, BALL_RADIUS, JUMP_HEIGHT)
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
    
    