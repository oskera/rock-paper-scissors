"""AI for for rock-paper-scissors games"""

class AI:
    """Single AI with n-length memory"""

    game = None
    n = 0
    moves = ['R', 'P', 'S']

    def __init__(self, game, n):
        self.game = game
        self.n = n

    def get_move(self):
        return None
