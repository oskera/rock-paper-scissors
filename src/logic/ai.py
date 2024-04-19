"""AI for for rock-paper-scissors games"""

import re


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
