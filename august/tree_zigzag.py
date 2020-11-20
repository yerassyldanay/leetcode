import math
from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        x = int(math.log(label, 2))
        print(x)

        result = []

        while x > 0:
            result.append(label)
            x = x - 1

            label = int(label / 2)
            label = int( math.pow(2, x + 1) - 1 + math.pow(2, x) - label )

            # print(label, x)

        result.append(1)
        result.reverse()

        return result

s = Solution()
a = s.pathInZigZagTree(13)
print(a)
