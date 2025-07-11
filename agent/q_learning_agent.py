import random
import numpy as np
from agent.policy import epsilon_greedy_policy

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        self.q_table = {} 
        self.actions = actions 
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        
    def get_q_value(self, state, action):
        return self.q_table.get(state, {}).get(action, 0.0)
    
    def set_q_value(self, state, action, value):
        if state not in self.q_table:
            self.q_table[state] = {}
        self.q_table[state][action] = value
        
    def choose_action(self, state, valid_actions):
        q_values = {a: self.get_q_value(state, a) for a in valid_actions}
        return epsilon_greedy_policy(q_values, valid_actions, self.epsilon)
        
    def learn(self, state, action, reward, next_state, next_valid_actions, done):
        current_q =  self.get_q_value(state, action)
        if done:
            target = reward
        else:
            future_q = [self.get_q_value(next_state, a) for a in next_valid_actions]
            target = reward + self.gamma * max(future_q)
        new_q = current_q + self.alpha * (target - current_q)
        self.set_q_value(state, action, new_q)