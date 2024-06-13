from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def test_prime_factors(self):
        prime_factor = PrimeFactors()
        self.assertEqual(2, prime_factor.of(2))

