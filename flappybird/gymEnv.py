import gym
from gym import spaces
import numpy as np
import pygame
from screen import GameScreen
from bird import Bird
from obstacle import Pipe
from const import *


class FlappyBirdEnv(gym.Env):
    def __init__(self):
        super(FlappyBirdEnv, self).__init__()
        pygame.init()

        # Initialize game components
        self.screen = GameScreen()
        self.bird = Bird(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.pipes = [Pipe(SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP)]

        # Define action and observation spaces
        self.action_space = spaces.Discrete(2)  # 0: No action, 1: Flap
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(SCREEN_WIDTH, SCREEN_HEIGHT, 3), dtype=np.uint8
        )

        self.clock = pygame.time.Clock()
        self.done = False
        self.score = 0

    def reset(self):
        # Reset game state
        self.bird = Bird(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.pipes = [Pipe(SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP)]
        self.score = 0
        self.done = False
        return self._get_observation()