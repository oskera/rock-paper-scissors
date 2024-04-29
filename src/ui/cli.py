"""Command Line Interface"""

class CLI:

    game = None
    ai = None

    def __init__(self, game, ai):
        self.game = game
        self.ai = ai

    def run(self):
        while True:
            self.play_round()

    def play_round(self):
        user_action = self.action()
        opponent_action = self.opponent_action()
        self.result(self.game.play(user_action, opponent_action))
        self.winlose()
        self.rounds()
        print("")


    def action(self):
        return input("Type your action: ")

    def opponent_action(self):
        opponent_action = self.ai.get_action()
        print(f"AI plays {opponent_action}")
        return opponent_action

    def result(self, result):
        if result == 0:
            print("Draw!")
        if result == 1:
            print("You win!")
        if result == -1:
            print("AI wins!")

    def winlose(self):
        winlose = self.game.winlose
        print(f"AI winrate is {winlose[0]/sum(winlose)}")

    def rounds(self):
        print(f"Rounds played: {sum(self.game.winlose)}")
