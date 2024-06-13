from unittest import TestCase

from baseballGame.game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_illegal_argument(self, guess_num):
        try:
            self.game.guess(guess_num)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_inputs(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")

