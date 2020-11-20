from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()

        print(range(0, len(s) - 10))

        for i in range(0, len(s) - 9):
            piece = s[i:i + 10]

            print(i, s[i:i+10], seen, piece in seen)

            if piece in seen:
                result.add(piece)
            else:
                seen.add(piece)

        return list(result)

s = Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))