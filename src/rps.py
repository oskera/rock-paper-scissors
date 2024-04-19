"""Main module"""

from logic.game import Game

game = Game()
game.play('R', 'P')
game.play('P', 'R')
game.play('S', 'P')
game.play('P', 'P')
print(game.action_history)