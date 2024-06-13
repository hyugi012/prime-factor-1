from unittest import TestCase

from baseballGame.game import Game


class TestGame(TestCase):
    def test_game(self):
        self.game = Game()
        with self.assertRaises(TypeError):
            self.game.guess(None)
