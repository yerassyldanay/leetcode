class Solution:
    def __init__(self):
        self.d = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0
        }

    def myAtoi(self, string: str) -> int:
        result = 0
        sign = 1
        valid = True

        for char in string:
            """
                1. skip space
                2. encountered minus, then take into consideration that the final value would be negative
                    a. encountered after space - valid
                    b. within numbers or other chracters - invalid
                3. encountered characters
                    a. not digit - return what you have
                    b. digit - store

                .. check range
            """

            if char in ['+', ' ', '-']:
                if not valid:
                    return self.check_range_and_return_valid_number(result * sign)

                if char == ' ':
                    continue

                if char == '-':
                    sign = -1

                valid = False

            else:
                if char not in self.d:
                    return self.check_range_and_return_valid_number(result * sign)

                # after this line we cannot have any sign
                valid = False

                result = result * 10 + self.d[char]

        return self.check_range_and_return_valid_number(result * sign)

    def check_range_and_return_valid_number(self, num):
        if 2 ** 31 - 1 < num:
            return 2 ** 31 - 1
        elif (-1) * (2 ** 31) > num:
            return (-1) * (2 ** 31)

        return num


s = Solution()
print(s.myAtoi("      -11919730356x"))

