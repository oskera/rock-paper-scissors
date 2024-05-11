import unittest
from logic.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_result_rr(self):
        game = Game()
        self.assertEqual(0, game.result("R", "R"))

    def test_result_rp(self):
        game = Game()
        self.assertEqual(-1, game.result("R", "P"))

    def test_result_rs(self):
        game = Game()
        self.assertEqual(1, game.result("R", "S"))

    def test_result_pr(self):
        game = Game()
        self.assertEqual(1, game.result("P", "R"))

    def test_result_pp(self):
        game = Game()
        self.assertEqual(0, game.result("P", "P"))

    def test_result_ps(self):
        game = Game()
        self.assertEqual(-1, game.result("P", "S"))

    def test_result_sr(self):
        game = Game()
        self.assertEqual(-1, game.result("S", "R"))

    def test_result_sp(self):
        game = Game()
        self.assertEqual(1, game.result("S", "P"))

    def test_result_ss(self):
        game = Game()
        self.assertEqual(0, game.result("S", "S"))

    def test_play(self):
        game = Game()
        self.assertEqual(-1, game.play("R", "P"))
