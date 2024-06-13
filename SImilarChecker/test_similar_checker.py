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


    def test_len_is_more_than_twice(self):
        str1 = "AB"
        str2 = "B"
        self.assertEqual(0, self.checker.check_length(str1, str2))

    def test_len_is_same(self):
        str1 = "AB"
        str2 = "BC"
        self.assertEqual(60, self.checker.check_length(str1, str2))

    def test_len_is_different(self):
        str1 = "AA"
        str2 = "BAA"
        self.assertEqual(30, self.checker.check_length(str1, str2))

