from typing import List

class Solution:
    def solve(self, arr: List[int]) -> List[List[int]]:
        leaves = [[]]

        for elem in arr:
            newLeaves = list()

            while leaves:
                node = leaves.pop()
                newLeaves.append(node.copy())
                node.append(elem)
                newLeaves.append(node)

            leaves = newLeaves

        # leaves.sort()
        return leaves

    def solve_better(self, n: int) -> List[List[int]]:

        self.sets = []

        def help(k: int) :
            if k == n:
                print(self.sets)
            else:
                help(k + 1)
                self.sets.append(k)
                help(k + 1)
                self.sets.pop()

        help(0)
        return []

    def solve_even_better(self, n: int) -> List[int]:

        for b in range(0, 1<<n):
            arr = []
            for i in range(0, n):
                print(b, 1<<i, b & (1<<i))
                if b & (1<<i):
                    arr.append(i)

            print(arr, end="\n\n")

        return []

s = Solution()
# a = s.solve([0, 1, 2])
# print(a)

s.solve_even_better(3)

