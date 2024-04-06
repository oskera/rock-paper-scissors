import re

class Game:
    """A class for handling game logic"""

    def play(self, action_1, action_2):
        """A method called to record and score a game"""

        # Check validity
        self.validate(action_1)
        self.validate(action_2)

    def validate(self, input):
        """A method for checking that input is valid"""
        input = input.upper()
        return input if re.match(r"^(R|P|S)$", input) else False


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