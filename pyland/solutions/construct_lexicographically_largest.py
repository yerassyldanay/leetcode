from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        position = [0] * (n * 2 - 1)
        seen = [False] * (n + 1)
        seen[0] = True

        def help(ri):
            while ri < len(position) and position[ri] != 0:
                ri = ri + 1

            if ri >= len(position):
                return True

            for numi, occurred in enumerate(seen[::-1]):
                num = len(seen) - numi - 1
                if occurred:
                    continue

                next_i = ri + num
                if num == 1:
                    next_i = ri

                if next_i >= len(position) or (position[next_i] != 0):
                    continue

                position[ri] = num
                position[next_i] = num

                # print(num, numi)
                seen[num] = True
                ok = help(ri + 1)
                if ok:
                    return True

                seen[num] = False

                position[ri] = 0
                position[next_i] = 0

            return False

        help(0)

        # print(self.val)
        return position


s = Solution()
a = s.constructDistancedSequence(20)
print(a)
