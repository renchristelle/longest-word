# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase
