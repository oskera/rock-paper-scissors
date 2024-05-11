import unittest
from logic.ai import AI, MultiAI
from logic.game import Game

class TestAI(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_ai_action(self):
        game = Game()
        ai = AI(game, 1, 1)
        for i in range(10):
            game.play("R", ai.get_action())
        self.assertEqual("P", ai.get_action())

    def test_multi_ai_action(self):
        game = Game()
        ai = MultiAI(game, 3)
        for i in range(10):
            game.play("R", ai.get_action())
            game.play("P", ai.get_action())
            game.play("S", ai.get_action())
        self.assertEqual("P", ai.get_action())
