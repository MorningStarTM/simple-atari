import pygame
import gym
from jumper import JumpEnv


import gym

# Register your custom environment
gym.envs.register(
    id='JumpEnv-v0',
    entry_point='__main__:JumpEnv',
)

# Create the environment
env = gym.make('JumpEnv-v0')

for i in range(10):
# Reset the environment to start
    observation = env.reset()

    # Example loop to take random actions
    done = False
    while not done:
        action = env.action_space.sample()  # Random action
        observation, reward, done, info = env.step(action)
        env.render()

env.close()