class Game:
    def guess(self, guess):
        if guess is None:
            raise TypeError()

        if len(guess) != 3:
            raise TypeError()

        if guess[0] == guess[1] or \
            guess[0] == guess[2] or \
            guess[1] == guess[2]:
            raise TypeError()


        for number in guess:
            if ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
