
import re

class Solution(object):
    def __init__(self):
        pass

    def prettify(self, binary):
        return "0" * (32 - len(binary)) + binary

    def binary_compare(self, first: str, second: str):
        first = self.prettify(first)
        second = self.prettify(second)

        for index, bit in enumerate(first):
            if bit > second[index]:
                return True
            elif bit < second[index]:
                return False

    def binary_sub(self, from_binary: str, binary: str):

        # convert them into an array
        from_binary = re.findall("\d", from_binary)
        binary = re.findall("\d", binary)

        for mindex in range(len(from_binary) - 1, -1, -1):
            if from_binary[mindex] >= binary[mindex]:
                result = int( from_binary[mindex]  ) - int( binary[mindex] )
                from_binary[mindex] = f"{result}"
            else:
                from_binary[mindex] = '1'
                index = mindex - 1

                while index >= 0:
                    if from_binary[index] == '0':
                        from_binary[index] = '1'
                    else:
                        from_binary[index] = '0'
                        break
                    index = index - 1

        return ''.join(from_binary)

    def binary_div(self, dividend, divisor):
        dividend = ''.join(re.findall("1[0-1]*", dividend))
        divisor = ''.join(re.findall("1[0-1]*", divisor))

        length = len(divisor)
        index = 0

        while len(dividend) > index:
            index = length
            while self.binary_compare(dividend[:index], divisor):
                index = index + 1

            result = self.binary_sub(''.join(dividend[:index]), divisor)
            dividend = result + dividend[index:]
            dividend = ''.join(re.findall("1[0-1]*", dividend))

        return dividend

s = Solution()
a = s.binary_div("100", "001")
print(a)

