import gym
from gym import spaces
import numpy as np
import pygame
import random
from .asteroid import Asteroid
from .jet import Jet
from .screen import GameScreen
from .const import *

class Invader(gym.Env):
    def __init__(self):
        super(Invader, self).__init__()
        pygame.init()

        # Initialize game components
        self.screen = GameScreen()
        
        self.action_space = spaces.Discrete(4)

        # Define the observation space: resized screen to 512x512 pixels
        self.observation_space = spaces.Box(low=0, high=255, shape=(512, 512, 3), dtype=np.uint8)

        # Initialize game state variables
        self.done = False


    def reset(self):
        # Reset the game to the initial state
        self.game.__init__()  # Reinitialize to reset game
        self.done = False
        return self._get_observation()