"""A module for handling game logic"""

import re


class Game:
    """A class for handling game logic"""

    action_history = ""
    winlose = [0, 0, 0]    # [ai wins, draw, player wins]

    def play(self, action_1, action_2):
        """A method called to record and score a game"""

        # Check validity
        action_1 = self.validate(action_1)
        action_2 = self.validate(action_2)
        if not action_1 and action_2:
            print("Error! Invalid input.")
            return

        self.update_action_history(action_1)

        # Scoring play
        result = self.result(action_1, action_2)
        self.update_winlose(result)
        return result

    def validate(self, input):
        """A method for checking that input is valid"""
        input = input.upper()
        return input if re.match(r"^(R|P|S)$", input) else False

    def update_action_history(self, action):
        self.action_history = self.action_history + action

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

    def update_winlose(self, result):
        self.winlose[result + 1] = self.winlose[result + 1] + 1
