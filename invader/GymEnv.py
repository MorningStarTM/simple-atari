import gym
from gym import spaces
import numpy as np
import pygame
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
        
        self.action_space = spaces.Discrete(4)  # Actions: 0 = No-op, 1 = Left, 2 = Right, 3 = Shoot

        # Define the observation space: resized screen to 64x64 pixels
        self.observation_space = spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8)

        self.clock = pygame.time.Clock()
        self.done = False

    def reset(self):
        # Reset the game to the initial state
        self.screen = GameScreen()  # Reinitialize to reset the game screen
        self.done = False
        return self._get_observation()
    
    def step(self, action):
        # Apply action to the game
        if action == 1:
            self.screen.jet1.move_left()
        elif action == 2:
            self.screen.jet1.move_right()
        elif action == 3:
            self.screen.jet1.shoot(self.screen.bullet_group)

        self.screen.create_asteroid()
        # Update the game state
        self.screen.update()

        # Check for collisions and update rewards
        reward = self._calculate_reward()

        # Check if the game is done
        self.done = self.screen.check_collision()  # Check collision directly from GameScreen

        # Get the next observation
        observation = self._get_observation()

        self.clock.tick(60)  # Limit the game to 60 FPS

        # Return the step information
        return observation, reward, self.done, {}
    
    def _calculate_reward(self):
        # Define reward mechanism
        reward = 0
        for bullet in self.screen.bullet_group:
            # If bullet hits an asteroid, give positive reward
            if pygame.sprite.spritecollide(bullet, self.screen.asteroid_group, True, pygame.sprite.collide_mask):
                reward += 1
        # Negative reward if the jet collides with an asteroid
        if self.screen.check_collision():
            reward -= 10
        return reward

    def _get_observation(self):
        # Capture the screen and resize it to 64x64
        obs = pygame.surfarray.array3d(pygame.display.get_surface())
        obs = np.transpose(obs, (1, 0, 2))  # Convert to (HEIGHT, WIDTH, 3)
        obs = pygame.transform.scale(pygame.surfarray.make_surface(obs), (64, 64))
        return pygame.surfarray.array3d(obs)
    
    def render(self, mode='human'):
        # Draw all game elements on the screen
        self.screen.draw()
        pygame.display.flip()  # Update the display

        # Properly handle Pygame events to avoid "not responding" state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
                break

    def close(self):
        pygame.quit()
