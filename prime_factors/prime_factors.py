class PrimeFactors:
    def __init__(self):
        pass

    def of(self, number) -> list:
        factors = []
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            divisor += 1

        return factors
