from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word: str) -> List[int]:
            p = {}
            result = []
            for letter in word:
                a = p.setdefault(letter, len(p))
                result.append(a)

            # print(p)
            return result

        pattern = convert(pattern)
        # print(pattern)

        for word in words:
            tpattern = convert(word)
            if tpattern == pattern:
                print(tpattern, pattern)
                yield word


class Solution2:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = self.create_pattern(pattern)
        return [word for word in words if pattern == self.create_pattern(word)]

    def create_pattern(self, word) -> list:
        d = {}
        a = [d.setdefault(letter, len(d)) for letter in word]
        print(a)
        return a

s = Solution2()
a = s.findAndReplacePattern(["mmmeqq", "qqqlrr", "aaaaajeeeee"], "aaabcc")
print(list(a))
