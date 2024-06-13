class Game:
    def guess(self, guess):
        if guess is None:
            raise TypeError()

        if len(guess) != 3:
            raise TypeError()

        for number in guess:
            if ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
