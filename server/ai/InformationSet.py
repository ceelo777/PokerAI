import numpy as np
import random

class InformationSet:
    def __init__(self, key, actions):        
        self.key = key
        self.regret_sum = np.zeros(actions)

        # Calculate the contribution from all the past strategies 
        # Do this by multiplying reach probability by strategy for each iteration
        self.strategy_sum = np.zeros(actions)
        self.actions = actions

        # Raw strategy evaluations
        self.strategy = np.repeat(1 / self.actions, self.actions)
        self.reach_pr = 0
        self.reach_pr_sum = 0

    def next_strategy(self):
        self.strategy_sum += self.reach_pr * self.strategy
        self.strategy = self.calc_strategy()
        self.reach_pr_sum += self.reach_pr
        self.reach_pr = 0

    def find_positive(self):
        return np.where(self.regret_sum > 0, self.regret_sum, 0)  
    
    def calc_strategy(self):
        # Calculate current strategy from the sum of regret
        strat = find_positive()
        count = sum(strat)        
        if (count > 0):
            # Normalizing the strategy array
            return strat / count
        else:
            # Reset the strategy
            strat = np.repeat(1 / self.actions, self.actions)
            return strat
    
    def get_avg_strategy(self):
        # Calculate average strategy - (strategy array / reach probability array)
        strat = self.strategy_sum / self.reach_pr_sum
        strat = np.where(strat < 0.001, 0, strategy)
        return sum(self.strategy) / len(self.strategy)
        