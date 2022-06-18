from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        l = 0
        for stone in stones:
            l = max(l, stone[0], stone[1])
        l = l + 1

        mat = []
        for i in range(l):
            mat.append([1] * (l))

        # print(mat)

        def dfs(mat: List[List[int]], y, x: int) -> int:
            count = 0
            if mat[y][x] == -1:
                mat[y][x] = 1
                count += 1

            l = len(mat)

            for yi in range(l):
                if mat[yi][x] == -1:
                    count += dfs(mat, yi, x)

            for xi in range(l):
                if mat[y][xi] == -1:
                    count += dfs(mat, y, xi)

            return count

        count = 0
        for stone in stones:
            y, x = stone
            mat[y][x] = -1

        for stone in stones:
            y, x = stone
            # print(y, x)
            if mat[y][x] == -1:
                mat[y][x] = 1
                count = count + dfs(mat, y, x)

        return count

a = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# a = [[0,0],[0,2],[1,1],[2,0],[2,2]]
a = [[0,0]]
a = []
s = Solution()
b = s.removeStones(a)
print(b)
