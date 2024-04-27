"""Main module"""

from logic.game import Game
from logic.ai import MultiAI

game = Game()
ai = MultiAI(game, 3)

game.play('P', ai.get_action())
game.play('P', ai.get_action())
game.play('P', ai.get_action())
game.play('P', ai.get_action())
game.play('P', ai.get_action())
game.play('P', ai.get_action())
print(game.winlose)
