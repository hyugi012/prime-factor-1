from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def test_prime_factor_of_1(self):
        prime_factor = PrimeFactors()
        self.assertEqual([], prime_factor.of(1))

