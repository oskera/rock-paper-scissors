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

class AI:
    """Single AI with n-length memory"""

    game = None
    n = 0
    actions = ['R', 'P', 'S']

    def __init__(self, game, n):
        self.game = game
        self.n = n

    def get_action(self):
        recent = self.get_recent()
        if len(recent) < self.n:
            return self.get_random()
        frequency = [0] * len(self.actions)
        for i in range(0, len(self.actions)):
            frequency[i] = self.count(recent + self.actions[i])
        next = self.actions[frequency.index(max(frequency))]
        return self.get_counter(next)

    def get_counter(self, action):
        if action == 'R':
            return 'P'
        elif action == 'P':
            return 'S'
        elif action == 'S':
            return 'R'

    def get_recent(self):
        return self.game.action_history[-self.n:]

    def count(self, sequence):
        return len(re.findall(f'(?={sequence})', self.game.action_history))

    def get_random(self):
        return self.actions[random.randint(0,len(self.actions) - 1)]
