class PrimeFactors:
    def __init__(self):
        pass

    def of(self, number) -> list:
        factors = []
        if number > 1:
            if number == 4:
                while number % 2 == 0:
                    factors.append(2)
                    number //= 2
            else:
                factors.append(number)

        return factors
