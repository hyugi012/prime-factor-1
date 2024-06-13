from unittest import TestCase

from baseballGame.game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def test_exceptipn_when_type_is_None(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)

    def test_exception_when_input_len_is_not_3(self):
        with self.assertRaises(TypeError):
            self.game.guess("12")