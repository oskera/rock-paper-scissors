"""AI for for rock-paper-scissors games"""

import random
import re


class MultiAI:
    """AI consisting of multiple single AIs"""

    game = None
    singles = []

    def __init__(self, game, f):
        self.game = game
        self.initialize_singles(f)

    def initialize_singles(self, f):
        for i in range(1, f + 1):
            self.singles = self.singles + [AI(self.game, i)]

    def get_best(self):
        winrate = []
        for ai in self.singles:
            winrate = winrate + [ai.get_win_rate()]
        return winrate.index(max(winrate))

class AI:
    """Single AI with n-length memory"""

    game = None
    action_history = ""
    n = 0
    actions = ['R', 'P', 'S']

    def __init__(self, game, n):
        self.game = game
        self.n = n

    def get_action(self):
        recent = self.get_recent_opponent()
        if len(recent) < self.n:
            action = self.get_random()
        else:
            frequency = [0] * len(self.actions)
            for i in range(0, len(self.actions)):
                frequency[i] = self.count(recent + self.actions[i])
            next = self.actions[frequency.index(max(frequency))]
            action = self.get_counter(next)
        self.update_history(action)
        return action

    def get_counter(self, action):
        if action == 'R':
            return 'P'
        elif action == 'P':
            return 'S'
        elif action == 'S':
            return 'R'

    def update_history(self, action):
        self.action_history = self.action_history + action

    def get_recent_self(self):
        return self.action_history[-self.n:]

    def get_recent_opponent(self):
        return self.game.action_history[-self.n:]

    def get_win_rate(self):
        recent_self = self.get_recent_self()
        recent_opponent = self.get_recent_opponent()
        wins = 0
        for i in range(0, self.n):
            action_self = recent_self[i]
            action_opponent = recent_opponent[i]
            if self.game.result(action_self, action_opponent) == 1:
                wins = wins + 1
        return wins/self.n

    def count(self, sequence):
        return len(re.findall(f'(?={sequence})', self.game.action_history))

    def get_random(self):
        return self.actions[random.randint(0,len(self.actions) - 1)]
