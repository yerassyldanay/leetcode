from typing import List

# [1, 2, 3, 4, 5]
# []
class Solution:
    def solve(self, arr: List[int]):
        length = len(arr)
        perm = list()
        used = [False] * len(arr)

        def find():
            if len(perm) == length:
                print(perm)
            else:
                for i in range(0, length, 1):

                    if used[i]:
                        continue

                    used[i] = True
                    perm.append(arr[i])

                    find()

                    used[i] = False
                    perm.pop()


        return find()

s = Solution()
s.solve([0, 1, 2])
