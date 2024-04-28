"""Main module"""

from logic.game import Game
from logic.ai import MultiAI
from ui.cli import CLI

game = Game()
cli = CLI(game, MultiAI(game, 5))
cli.run()
