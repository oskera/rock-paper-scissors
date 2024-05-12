import unittest
from logic.ai import MultiAI
from logic.game import Game

class TestAI(unittest.TestCase):
    def setUp(self):
        pass

    def test_ai_action(self):
        game = Game()
        ai = MultiAI(game, 1)
        for i in range(10):
            game.play("R", ai.get_action())
        self.assertEqual("P", ai.get_action())

    def test_multi_ai_action_3(self):
        game = Game()
        ai = MultiAI(game, 3)
        for i in range(10):
            game.play("R", ai.get_action())
            game.play("R", ai.get_action())
            game.play("P", ai.get_action())
        game.play("R", ai.get_action())
        game.play("R", ai.get_action())
        self.assertEqual("S", ai.get_action())

    def test_multi_ai_action_5(self):
        game = Game()
        ai = MultiAI(game, 5)
        for i in range(10):
            game.play("R", ai.get_action())
            game.play("R", ai.get_action())
            game.play("P", ai.get_action())
            game.play("P", ai.get_action())
            game.play("S", ai.get_action())
        game.play("R", ai.get_action())
        game.play("R", ai.get_action())
        game.play("P", ai.get_action())
        game.play("P", ai.get_action())
        self.assertEqual("R", ai.get_action())
