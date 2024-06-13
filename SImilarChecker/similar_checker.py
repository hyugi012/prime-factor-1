class SimilarChecker:

    def check_length(self, str1, str2):
        self.assert_illegal_input(str1)
        self.assert_illegal_input(str2)
        pass

    def assert_illegal_input(self, s):
        if s is None:
            raise TypeError

        for char in s:
            if not ord("A") <= ord(char) <= ord("Z"):
                raise TypeError
