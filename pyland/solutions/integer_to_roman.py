
"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
class Solution:
    d = {
        "0": "",
        "1": "I",
        "5": "V",
        "10": "X",
        "50": "L",
        "100": "C",
        "500": "D",
        "1000": "M",
        "5000": "N",
        "10000": "H",
    }

    def intToRomanHelp(self, left, lcount, right, rcount: int) -> str:
        return self.d[f"{left}"] * lcount + self.d[f"{right}"] * rcount

    def intToRoman(self, num: int) -> str:
        num = f"{num}"
        returnString = ""
        for index, digit in enumerate(num):
            length = len(num[index + 1:])
            digit = int(digit)
            if f"{ digit * (10**length) }" in self.d:
                returnString = returnString + self.d[f"{ digit * (10**length) }"]
                continue

            if digit > 5:
                if 10 - digit - 1 <= 0:
                    returnString = returnString + self.intToRomanHelp(10**length, 10 - digit, 10 * (10 ** length), 1)
                else:
                    returnString = returnString + self.intToRomanHelp(5 * (10**length), 1, 10 ** length, digit - 5)
            else:
                if 5 - digit - 1 <= 0:
                    returnString = returnString + self.intToRomanHelp(10**length, 5 - digit, 5 * (10 ** length), 1)
                else:
                    returnString = returnString + self.intToRomanHelp(1 * (10**length), 0, 10 ** length, digit)


        return returnString

s = Solution()
for i in range(40000):
    print(i, " >> ", s.intToRoman(i))

