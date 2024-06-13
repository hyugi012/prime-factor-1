class SimilarChecker:

    def check_length(self, str1, str2):
        self.assert_illegal_input(str1)
        self.assert_illegal_input(str2)
        pass

    def check_alpha(self, str1, str2):
        str1_set = set()
        str2_set = set()
        for s1 in str1:
            str1_set.add(s1)
        for s2 in str2:
            str2_set.add(s2)

        if str1_set & str2_set is set():
            return 0
        if str1_set | str2_set == str1_set:
            return 40
        return int((len(str1_set & str2_set) / len(str1_set | str2_set)) * 40)

    def assert_illegal_input(self, s):
        if s is None:
            raise TypeError

        for char in s:
            if not ord("A") <= ord(char) <= ord("Z"):
                raise TypeError
