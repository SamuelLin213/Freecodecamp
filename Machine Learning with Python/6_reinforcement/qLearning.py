# Q-learning: involves learning a matrix of action-reward values(often referred to
    # as Q-Table or Q-Matrix); shape of number of possible states x number of possible actions
    # value at matrix[m, n] represents reward at state m and action n
# E.g. Navigate a frozen lake environment via Open AI's gym library

import gym   # all you have to do to import and use open ai gym!

# deal with "No available video device" error
import os
os.environ['SDL_VIDEODRIVER']='dummy'
import pygame
pygame.display.set_mode((640,480))

env = gym.make('FrozenLake-v1', new_step_api=True, render_mode='human')  # we are going to use the FrozenLake enviornment

# print out states and actions
print(env.observation_space.n)   # get number of states
print(env.action_space.n)   # get number of actions

env.reset()  # reset enviornment to default state

action = env.action_space.sample()  # get a random action from all available actions

new_state, reward, done, info = env.step(action)  # take action, notice it returns information about the action

env.render() # render GUI for environment

# Frozen lake environment
import gym
import numpy as np
import time

# build empty Q-table
env = gym.make('FrozenLake-v1', new_step_api=True, render_mode='human')  # we are going to use the FrozenLake enviornment
STATES = env.observation_space.n
ACTIONS = env.action_space.n

Q = np.zeros((STATES, ACTIONS))  # create a matrix with all 0 values

EPISODES = 1500 # how many times to run the enviornment from the beginning
MAX_STEPS = 100  # max number of steps allowed for each run of enviornment

LEARNING_RATE = 0.81  # learning rate
GAMMA = 0.96

RENDER = True;

epsilon = 0.9  # start with a 90% chance of picking a random action

rewards = []
for episode in range(EPISODES):

  state = env.reset()
  for item in range(MAX_STEPS):

    if RENDER:
      env.render()

    # picks action
    if np.random.uniform(0, 1) < epsilon: # check if randomly selected value is less than epilson
      action = env.action_space.sample()  # take random action
    else:
      action = np.argmax(Q[state, :]) # use Q table to pick best action based on current value

    next_state, reward, done, truncated, item = env.step(action)

    Q[state, action] = Q[state, action] + LEARNING_RATE * (reward + GAMMA * np.max(Q[next_state, :]) - Q[state, action])

    state = next_state

    if done:
      rewards.append(reward)
      epsilon -= 0.001
      break  # reached goal

print(Q)
print(f"Average reward: {sum(rewards)/len(rewards)}:")
# and now we can see our Q values!
