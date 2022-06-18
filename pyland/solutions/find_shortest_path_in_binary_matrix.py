from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        deltas = [(-1, -1), (0, -1), (1, -1),  (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        if grid[0][0] != 0:
            return -1

        ylen = len(grid)
        xlen = len(grid[0])

        seen = set()

        def dfs(y, x, cost: int):

            if x == xlen - 1 and y == ylen - 1 and grid[y][x] != 1:
                return cost

            route = float('inf')
            if grid[y][x] == 1:
                return route

            for (dy, dx) in deltas:

                ny = y + dy
                nx = x + dx

                # print(y, x)
                # print(ny, nx, seen)
                # print()

                if 0 > ny or ny >= ylen:
                    continue

                if 0 > nx or nx >= xlen:
                    continue

                # if ny == 0 and nx == 2:
                    # print(seen)
                    # print(grid[ny][nx])

                if (ny, nx) in seen:
                    continue

                seen.add((ny, nx))
                nroute = dfs(ny, nx, cost + 1)
                route = min(route, nroute)
                seen.remove((ny, nx))

            return route

        seen.add((0, 0))
        route = dfs(0, 0, 1)
        if route == float('inf'):
            return -1
        return route

s = Solution()
grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
a = s.shortestPathBinaryMatrix(grid)
print(a)
