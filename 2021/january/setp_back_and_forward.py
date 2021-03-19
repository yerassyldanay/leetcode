from collections import defaultdict as dd
from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:

        dont = set()
        q = deque()
        q.append((0, 0, True))
        seen = set()
        for each in forbidden:
            dont.add(each)

        limited = x + a * 100

        # -------------------------------

        while q:
            elem = q.popleft()
            pos, count, backed = elem

            if elem in seen:
                continue

            seen.add(elem)

            if pos == x:
                # print(pos, x)
                return count

            count = count + 1
            if pos - b >= 0 and not backed and pos - b not in dont:
                # print("  ", pos - b, pos, b)
                q.append((pos - b, count, True))

            t = a
            i = 0
            while pos + t < limited and pos + t not in dont:
                # print(">>>", pos + t, pos, t)
                q.append((pos + t, count + i, False))
                t += a
                i += 1

            # print(q)

        return -1


# s = Solution()
# # print("-------------------------------------------")
# a = s.minimumJumps([8, 3, 16, 6, 12, 20], 15, 13, 11)
# print(a)
# print("-------------------------------------------")
# s = Solution()
# a = s.minimumJumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7)
# print(a)

s = Solution()
a = s.minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29, 98, 80)
print(a)
