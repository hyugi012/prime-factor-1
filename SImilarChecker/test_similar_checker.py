from unittest import TestCase, skip

from SImilarChecker.similar_checker import SimilarChecker


class TestSimilarChecker(TestCase):

    def setUp(self):
        super().setUp()
        self.checker = SimilarChecker()

    def assert_illegal_input(self, str1, str2):
        try:
            self.checker.check_length(str1, str2)
            self.fail()
        except TypeError:
            pass

    def test_assert_invalid_inputs(self):
        self.assert_illegal_input(None, None)
        self.assert_illegal_input("abc", "AbC")
        self.assert_illegal_input("123", "12A")

    def test_same_alpha(self):
        self.assertEqual(40, self.checker.check_alpha("AB", "BA"))

    def test_different_alpha(self):
        self.assertEqual(0, self.checker.check_alpha("A","B"))

    def test_some_same_alpha(self):
        self.assertEqual(20, self.checker.check_alpha("AA", "AAE"))