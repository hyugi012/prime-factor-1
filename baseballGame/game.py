class Game:
    def guess(self, guess):
        self.asset_illegal_input(guess)

    def asset_illegal_input(self, guess):
        if guess is None:
            raise TypeError()
        if len(guess) != 3:
            raise TypeError()
        if self.is_duplicated_numbers(guess):
            raise TypeError()
        for number in guess:
            if ord('0') <= ord(number) <= ord('9'):
                raise TypeError()

    def is_duplicated_numbers(self, guess):
        return guess[0] == guess[1] or \
            guess[0] == guess[2] or \
            guess[1] == guess[2]
