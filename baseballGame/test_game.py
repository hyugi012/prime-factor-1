from unittest import TestCase

from baseballGame.game import Game
from baseballGame.game_result import GameResult


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
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def assert_matched_numbers(self, result, solved, strikes, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strikes, result.get_strikes())
        self.assertEqual(balls, result.get_balls())

    def generate_question(self, question_number):
        self.game.question = question_number

    def test_return_solve_if_matched(self):
        self.generate_question("123")
        self.assert_matched_numbers(self.game.guess("123"), True, 3, 0)

    def test_return_solve_if_not_matched(self):
        self.generate_question("123")
        self.assert_matched_numbers(self.game.guess("456"), False, 0, 0)

    def test_return_solve_if_some_matched(self):
        self.generate_question("123")
        self.assert_matched_numbers(self.game.guess("120"), False, 2, 0)