"""Main module"""

from logic.game import Game
from logic.ai import AI

game = Game()
ai = AI(game, 1)
game.play('R', 'P')
game.play('R', 'R')
game.play('R', 'R')
game.play('P', 'P')
game.play('R', 'P')
print(ai.get_action())
