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
    
    def _get_observation(self):
        # Render the game and return the screen state
        self.screen.update(self.bird, self.pipes)
        obs = pygame.surfarray.array3d(pygame.display.get_surface())
        return np.transpose(obs, (1, 0, 2))  # Transpose to (height, width, channels)
    

    def step(self, action):
        # Handle actions: 0 for no action, 1 for flap
        if action == 1:
            self.bird.flap()

        # Update bird and pipes
        self.bird.update()
        for pipe in self.pipes:
            pipe.move()

        # Check for collision
        reward = 1  # Default reward for staying alive
        if self._check_collision():
            reward = -100
            self.done = True

        # Check if pipes go off-screen and generate new pipes
        self._handle_pipes()

        # Calculate reward and check for game over
        self._check_score()
        observation = self._get_observation()

        return observation, reward, self.done, {}
    

    def _check_collision(self):
        # Check if bird collides with pipes or ground/ceiling
        bird_rect = self.bird.get_rect()
        if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
            return True
        for pipe in self.pipes:
            if bird_rect.colliderect(pipe.get_rect()):
                return True
        return False


    def _handle_pipes(self):
        # Remove off-screen pipes and generate new ones
        for pipe in self.pipes:
            if pipe.is_off_screen():
                self.pipes.remove(pipe)
                self.score += 1
        if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - PIPE_GAP * 1.5:
            self.pipes.append(Pipe(SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP))


    def _check_score(self):
        # Score increases when bird passes through pipes
        for pipe in self.pipes:
            if not pipe.passed and pipe.x < self.bird.x:
                self.score += 1
                pipe.passed = True

    def render(self, mode="human"):
        pygame.display.flip()
        self.clock.tick(60)

    def close(self):
        pygame.quit()