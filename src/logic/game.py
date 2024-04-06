class Game:
    """A class for handling game logic"""

    def result(self, action_1, action_2):
        """A method for scoring a Rock-Paper-Scissors game"""
        if action_1 == action_2:
            return 0
        elif action_1 == 'R' and action_2 == 'S':
            return 1
        elif action_1 == 'P' and action_2 == 'R':
            return 1
        elif action_1 == 'S' and action_2 == 'P':
            return 1
        else:
            return -1