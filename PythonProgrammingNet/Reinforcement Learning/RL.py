"""
Reinforcement Learning w/ Python Tutorial
1. Q-Learning introduction and Q Table
2. Q Algorithm and Agent (Q-Learning)
3. Q-Learning Analysis
4. Q-Learning In Our Own Custom Environment
5. Deep Q Learning and Deep Q Networks (DQN) Intro and Agent
6. Training Deep Q Learning and Deep Q Networks (DQN) Intro and Agent
"""
# coding:utf-8
import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

print(discrete_os_win_size)

q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))
print(q_table.shape)
print(q_table)

done = False

while not done:
    action = 2 # 0: Left, 1: Stop, 2: Right
    new_state, reward, done, _ = env.step(action)
    print(reward, new_state)
    env.render()
env.close()
