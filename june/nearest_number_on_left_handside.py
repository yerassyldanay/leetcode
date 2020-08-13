from typing import List

class Solution:
    def findCircleNum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        uni = list(range(n))

        for y in range(n):
            for x in range(n):
                if arr[y][x] == 1 and y != x:
                    self.Union(uni, y, x)

        print(uni)

        count = 0
        for i, elem in enumerate(uni):
            if elem == i:
                count += 1

        return count

    def Find(self, uni: List[int], i: int):
        if uni[i] == i:
            return i
        return self.Find(uni, uni[i])

    def Union(self, uni: List[int], y, x: int) -> None:
        yi = self.Find(uni, y)
        xi = self.Find(uni, x)
        if yi != xi:
            uni[yi] = xi


# a = [[1,1,0], [1,1,0], [0,0,1]]
# a = [[1,1,1], [1,1,1], [1,1,1]]
a = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
# a = [[1,1,0,0,0,0,0,1,0,1],[1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,0,1,1,0,0],[1,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,1,1],[1,0,0,0,0,0,0,0,1,1]]
s = Solution()
b = s.findCircleNum(a)
print(b)

