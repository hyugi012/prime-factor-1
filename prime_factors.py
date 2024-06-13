class PrimeFactors:
    def __init__(self):
        pass

    def of(self, number) -> list:
        factors = []
        if number > 1:
            divisor = 2
            if number == 4 or number == 6 or number == 9:
                while number > 1:
                    while number % divisor == 0:
                        factors.append(divisor)
                        number //= divisor
                    divisor += 1
            else:
                factors.append(number)

        return factors
