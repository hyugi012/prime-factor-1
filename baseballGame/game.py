class Game:
    def guess(self, guess):
        if guess is None:
            raise TypeError

        if len(guess) != 3:
            raise TypeError