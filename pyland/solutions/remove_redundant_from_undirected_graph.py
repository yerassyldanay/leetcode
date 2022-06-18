from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        maxim = 0
        for each in edges:
            maxim = max(maxim, each[0], each[1])

        uni = list(range(maxim + 1))

        for pair in edges:
            f = self.Find(uni, pair[0])
            s = self.Find(uni, pair[1])
            if f == s:
                return pair

            self.Union(uni, f, s)

        return []

    def Find(self, arr: list, i: int) -> int:
        if arr[i] == i:
            return i
        return self.Find(arr, arr[i])

    def Union(self, arr: list, yi, xi: int) -> None:
        # yi = self.Find(arr, y)
        # xi = self.Find(arr, x)
        if yi != xi:
            arr[xi] = arr[yi]

a = [[1,2],[1,3],[2,3]]
a = [[1,2], [2,3], [3,4], [1,4], [1,5]]
a = [[1,5],[3,4],[3,5],[4,5],[2,4]]
s = Solution()
b = s.findRedundantConnection(a)
print(b)

