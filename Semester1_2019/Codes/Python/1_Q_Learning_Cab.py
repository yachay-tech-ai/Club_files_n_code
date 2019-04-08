# -*- coding: utf-8 -*-
# Importing the libraries
import gym
from time import sleep
import numpy as np
from random import uniform


# Training cab
env = gym.make("Taxi-v2").env
q_table = np.zeros([env.observation_space.n, env.action_space.n])
# Parameters for Bellman Equation
alpha = 0.1
gamma = 0.6
threshold = 0.1

for i in range(1, 100001):
    state = env.reset()
    while True:
        if uniform(0, 1) < threshold:
            action = env.action_space.sample() # Choose a random action
        else:
            action = np.argmax(q_table[state]) # Choose an action based on Q-Table

        next_state, reward, done, info = env.step(action) 
        old_value = q_table[state, action]
        next_max = max(q_table[next_state])    
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max) # Apply Bellman Equation
        q_table[state, action] = new_value # Update the Q-Table
        state = next_state
        
        if done:
            break
        
    if i % 1000 == 0:
        print(f"Training Episode: {i}")

print("Training finished.")


#Evaluating the performance of a random agent
total_steps, total_penalties = 0, 0
episodes = 100

for _ in range(episodes):
    state = env.reset()
    while True:
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)

        if reward == -10:
            total_penalties += 1

        total_steps += 1
        if done:
            break

print(f"Results after {episodes} episodes:")
print(f"Average steps per episode: {total_steps / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")


#Evaluating the performance of a Q-Learning agent
total_steps, total_penalties = 0, 0
episodes = 100

for _ in range(episodes):
    state = env.reset()
    while True:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            total_penalties += 1

        total_steps += 1
        if done:
            break

print(f"Results after {episodes} episodes:")
print(f"Average steps per episode: {total_steps / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")


#Visualizing the results of Q-Learning
def printEnv(frames):
    for frame in frames:
        print(frame.getvalue())
        sleep(1)

state = env.reset()      
frames = [] 

while True:
    action = np.argmax(q_table[state])
    state, reward, done, info = env.step(action)
    frames.append(env.render(mode='ansi'))
    if done:
        break

printEnv(frames)