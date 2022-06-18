
class Solution:
    phone_dict = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    def letterCombinations(self, digits):
        return self.relateListToList([], digits)

    def relateListToList(self, prevList, leftDigits):
        if len(leftDigits) == 0:
            return prevList

        temp = leftDigits[0]
        result = []

        if len(prevList) == 0:
            return self.relateListToList(self.phone_dict[temp], leftDigits[1:])

        for character in self.phone_dict[temp]:
            for prevString in prevList:
                result.append(prevString + character)

        return self.relateListToList(result, leftDigits[1:])

s = Solution()
if __name__ == '__main__':
    a = s.letterCombinations("23")
    print(a)