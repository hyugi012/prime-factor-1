from baseballGame.game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess):
        self.asset_illegal_input(guess)
        if self.is_solved(guess):
            return self.get_success_result()
        else:
            balls, strikes = self.get_unsolved_result(guess)
            return GameResult(False, strikes, balls)

    def get_unsolved_result(self, guess):
        strikes = 0
        balls = 0
        for i in range(len(self.question)):
            if self.question.find(guess[i]) == i:
                strikes += 1
            elif self.question.find(guess[i]) > -1:
                balls += 1
        return balls, strikes

    def get_success_result(self):
        return GameResult(True, 3, 0)

    def is_solved(self, guess):
        return guess == self.question

    def asset_illegal_input(self, guess):
        if guess is None:
            raise TypeError
        if len(guess) != 3:
            raise TypeError
        if self.is_duplicated_numbers(guess):
            raise TypeError
        for number in guess:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError

    def is_duplicated_numbers(self, guess):
        return guess[0] == guess[1] or \
            guess[0] == guess[2] or \
            guess[1] == guess[2]
