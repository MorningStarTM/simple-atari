import gym
from gym import spaces
import numpy as np
import pygame
from .jet import Jet
from .screen import DynamicGameScreen
from .const import *


class JetEnv(gym.Env):
    def __init__(self):
        super(JetEnv, self).__init__()
        
        # Define action and observation space
        # Actions: [0] -> No action, [1] -> Rotate Left, [2] -> Rotate Right, [3] -> Accelerate, [4] -> Decelerate
        self.action_space = spaces.Discrete(5)
        
        # Observation space: [Jet X, Jet Y, Jet Angle, Jet Velocity]
        """self.observation_space = spaces.Box(
            low=np.array([0, 0, -180, 0]), 
            high=np.array([SCREEN_WIDTH, SCREEN_HEIGHT, 180, 5]),
            dtype=np.float32
        )"""

        self.observation_space = spaces.Box(
            low=0, high=255, shape=(SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8
        )

        # Initialize the game
        pygame.init()
        self.game_screen = DynamicGameScreen()
        self.jet = Jet(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Initial state
        self.state = self.get_state()
        self.frame = 0

    def reset(self):
        # Reset the environment to its initial state
        self.jet = Jet(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.game_screen = DynamicGameScreen()
        self.state = self._get_observation()
        return self.state

    def step(self, action):
        self.frame += 1
        # Execute one time step within the environment
        if action == 1:
            self.jet.rotate(left=True)
        elif action == 2:
            self.jet.rotate(right=True)
        elif action == 3:
            self.jet.move_forward()
        elif action == 4:
            self.jet.move_backward()

        # Move the jet based on its velocity and angle
        self.jet.move()

        # Calculate camera offset based on the jet's position
        jet_x, jet_y = self.jet.get_position()
        offset_y = jet_y - SCREEN_HEIGHT // 2

        # Update the game screen
        self.game_screen.update(0, offset_y)

        # Draw the jet on the screen
        self.jet.draw(self.game_screen.screen, offset_y)

        # Check for collision
        player_rect = self.jet.img.get_rect(topleft=(self.jet.x, self.jet.y))
        player_mask = pygame.mask.from_surface(self.jet.img)
        collision = self.game_screen.check_collision(player_rect, player_mask)

        # Determine reward
        if collision:
            reward = -100  # High penalty for collision
            self.frame = 0
            done = True
        
        # Check if the player has reached the end line
        elif self.jet.y <= -SCREEN_HEIGHT * 4:
            reward = 100  # High reward for reaching the end
            self.frame = 0
            done = True
        
        elif self.frame % 50 == 0:
            reward = -0.01
            done = False
        else:
            reward = 0.001  # Small reward for staying alive
            done = False

        return self._get_observation(), reward, done, {}

    def render(self, mode='human'):
        pygame.display.flip()

    def _get_observation(self):
        """Capture the screen and return it as an observation."""
        screen_array = pygame.surfarray.array3d(self.game_screen.screen)
        return np.transpose(screen_array, (1, 0, 2))

    def close(self):
        pygame.quit()

    def get_state(self):
        jet_x, jet_y = self.jet.get_position()
        return np.array([jet_x, jet_y, self.jet.angle, self.jet.vel], dtype=np.float32)
