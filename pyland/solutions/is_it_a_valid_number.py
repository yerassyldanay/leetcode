class Solution:
    def __init__(self):
        self.num = 0
        self.exp = 0
        self.sign = 0
        self.dot = 0
        self.digit_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def isNumber(self, s: str) -> bool:
        for i, char in enumerate(s):
            if char == 'e':
                return self.isNumberHelper(s[:i]) and self.isNumberHelper(s[i + 1:])

        return self.isNumberHelper(s)

    def isNumberHelper(self, s: str) -> bool:
        s = s.strip()

        if not s:
            return False

        for j, char in enumerate(s):

            #
            # example:
            #           0  .  1  2
            #  i  0  1  2  3  4  5
            #  j        0  1  2  3

            i = j + 2

            if char == '.':
                #
                #
                #
                if j == 0:
                    #
                    # after '.' there must be only digit
                    #   '.2e4564'
                    ok = (len(s) > 1 and s[j + 1] in self.digit_set)
                    if not ok:
                        return False

                    self.dot = i
                    continue

                #
                # invalid if it is '-.' or '+.'
                #
                if self.sign:
                    if s[j - 1] == '-' or s[j - 1] == '+':
                        if j != 1:
                            return False
                        else:
                            self.dot = i
                            continue
                #
                # encountered .
                #   it must come only after digits
                #
                if not self.num or self.exp or self.dot:
                    return False

                self.dot = i

            elif char in self.digit_set:
                #
                # digit can come after + / - / . / e / digit
                #
                self.num = i
                continue

            elif char == 'e':
                #
                # ok if '4e....', invalid if 'e...'
                # invalid '262.e...'
                if not self.num or self.exp or self.dot == i - 1:
                    return False

                self.exp = i

            elif char == '-' or char == '+':
                if j != 0 and not (self.exp and self.exp == i - 1):
                    return False

                # not need but worth
                self.sign = i

            else:
                return False

        last_char = s[len(s) - 1]
        if last_char not in self.digit_set:
            if len(s) == 1:
                return False

            if not (last_char == '.' and s[len(s) - 2] in self.digit_set):
                return False

        return True


s = Solution()
print(s.isNumber("156.e-64"))

