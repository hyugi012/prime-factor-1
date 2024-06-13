class SimilarChecker:
    def __init__(self):
        self.long_str = ""
        self.short_str = ""

    def check_length(self, str1, str2):
        self.assert_illegal_input(str1)
        self.assert_illegal_input(str2)

        self.long_str, self.short_str = self.compare_length(str1, str2)

        if len(self.long_str) >= len(self.short_str) * 2:
            return 0

        if len(self.long_str) == len(self.short_str):
            return 60

        gap = len(self.long_str) - len(self.short_str)
        return int((1 - (gap / len(self.short_str))) * 60)

    def compare_length(self, str1, str2):
        if len(str1) > len(str2):
            return str1, str2
        return str2, str1

    def assert_illegal_input(self, s):
        if s is None:
            raise TypeError

        for char in s:
            if not ord("A") <= ord(char) <= ord("Z"):
                raise TypeError
