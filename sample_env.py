import pygame
import gym
from jumper import JumpEnv
from navigator import JetEnv
from flappybird import FlappyBirdEnv
from invader import Invader
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def jumpenv():
    # Register your custom environment
    gym.envs.register(
        id='JumpEnv-v0',
        entry_point='__main__:JumpEnv',
    )

    # Create the environment
    env = gym.make('JumpEnv-v0')

    for i in range(10):
        total_reward = 0
    # Reset the environment to start
        observation = env.reset()
        # Example loop to take random actions
        done = False
        while not done:
            action = env.action_space.sample()  # Random action
            observation, reward, done, info = env.step(action)
            total_reward += reward
            env.render()
        print(f"Reward : {total_reward}")

    env.close()



def Jetenv():
    gym.envs.register(
        id='JetEnv-v0',
        entry_point='__main__:JetEnv',
    )

    env = gym.make('JetEnv-v0')

    for i in range(10):
        total_reward = 0
    # Reset the environment to start
        observation = env.reset()
        # Example loop to take random actions
        done = False
        while not done:
            action = env.action_space.sample()  # Random action
            observation, reward, done, info = env.step(action)
            total_reward += reward
            #env.render()
        print(f"Reward : {total_reward}")

    env.close()

def Flappyenv():
    gym.envs.register(
        id='FlappyEnv-v0',
        entry_point='__main__:FlappyBirdEnv',
    )

    env = gym.make('FlappyEnv-v0')
    print(f"Obs shape : {env.observation_space.shape}")

    for i in range(3):
        total_reward = 0
    # Reset the environment to start
        observation = env.reset()
        # Example loop to take random actions
        done = False
        while not done:
            action = env.action_space.sample()  # Random action
            observation, reward, done, info = env.step(action)
            total_reward += reward
            env.render()
        print(f"Reward : {total_reward}")

    env.close()



def space_invader():
    # Register the environment
    gym.envs.registration.register(
        id='SpaceInvader-v0',
        entry_point='__main__:Invader',
    )

    # Create the environment
    env = gym.make('SpaceInvader-v0')

    # Example of running the environment
    for episode in range(2):
        observation = env.reset()
        done = False
        total_reward = 0

        while not done:
            # Sample a random action
            action = env.action_space.sample()

            # Step the environment
            observation, reward, done, info = env.step(action)
            total_reward += reward

            # Render the environment
            env.render()

        print(f"Episode {episode + 1} finished with total reward: {total_reward}")

    env.close()


if __name__ == "__main__":
    space_invader()
    

