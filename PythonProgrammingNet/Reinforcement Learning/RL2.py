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

LEARNING_RATE = 0.1
DISCOUNT = 0.95 # weigth
EPISODES = 25000

SHOW_EVERY = 2000

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

epsilon = 0.5
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2

epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)

q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))


for episode in range(EPISODES):
    if episode % SHOW_EVERY == 0:
        print(episode)
        render = True
    else:
        render = False
    discrete_state = get_discrete_state(env.reset())

    #print(discrete_state)
    #print(q_table[discrete_state])
    #print(np.argmax(q_table[discrete_state]))

    done = False

    while not done:

        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state]) # 0: Left, 1: Stop, 2: Right
        else:
            action = np.random.randint(0, env.action_space.n)
        new_state, reward, done, _ = env.step(action)

        new_discrete_state = get_discrete_state(new_state)
        if render:
            env.render()
        if not done:
            max_future_q = np.max(q_table[discrete_state])
            current_q = q_table[discrete_state + (action, )]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action, )] * new_q
        elif new_state[0] >= env.goal_position:
            print("We made it on episode {}",format(episode))
            q_table[discrete_state + (action, )] = 0

        discrete_state = new_discrete_state

    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value
    
env.close()
