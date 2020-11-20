class Solution:
    def numIslands(self, grid: list) -> int:

        if not grid:
            return 0

        self.count = 0
        self.grid = grid

        def check(y, x):
            if x < 0 or x >= len(self.grid[0]):
                return False
            if y < 0 or y >= len(self.grid):
                return False
            return True

        def dfs(y, x):

            if not check(y, x):
                return

            if self.grid[y][x] == '1':
                self.grid[y][x] = 'v'
                for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(y + a, x + b)
                return

            if self.grid[y][x] == '0':
                self.grid[y][x] = 'v'

            return

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):

                if self.grid[y][x] == '1':
                    self.count += 1
                    dfs(y, x)

        # print(self.grid)
        return self.count


a = [["1","1","1"],["0","0","0"],["1","1","1"]]
s = Solution()
print(s.numIslands(a))

