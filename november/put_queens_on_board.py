from typing import List

class Solution:
    def print(self, board: List[List[int]]):
        for row in board:
            for elem in row:
                if elem:
                    print("X", end="  ")
                else:
                    print("O", end="  ")

            print()
        print()

    def rdiagonal(self, ty, tx, board):
        n = len(board)
        rdiagonal = False
        while True:
            if 0 > ty or ty >= n:
                return rdiagonal

            while True:
                if 0 > tx or tx >= n:
                    return rdiagonal

                rdiagonal |= board[ty][tx]
                ty -= 1
                tx -= 1

    def ldiagonal(selfself, ty, tx, board):
        n = len(board)
        ldiagonal = False
        while True:
            if ty < 0 or ty >= n:
                return ldiagonal

            while True:
                if tx < 0 or tx >= n:
                    return ldiagonal

                ldiagonal |= board[ty][tx]
                ty -= 1
                tx += 1

    def put(self, n: int):
        board = [[False] * n for _ in range(n)]
        result = [0]

        def nextOne(counter: int, y: int):
            if counter == n:
                # this is a solution
                result[0] += 1
                self.print(board)
                return

            if y >= n:
                return

            for x in range(0, n, 1):

                vertical = False
                for ty in range(0, y):
                    vertical |= board[ty][x]

                rdiagonal = self.rdiagonal(y, x, board)
                ldiagonal = self.ldiagonal(y, x, board)

                if vertical or rdiagonal or ldiagonal:
                    continue

                board[y][x] = True
                # self.print(board)

                nextOne(counter + 1, y + 1)

                board[y][x] = False

        nextOne(0, 0)
        return result[0]

    def put_efficiently(self, n: int):
        ldiag = [False] * (2 * n - 1)
        rdiag = [False] * (2 * n - 1)
        vertic = [False] * n
        resource = [0]

        board = [[False] * n for _ in range(n)]

        def find(counter: int, y: int):
            if counter == n:
                self.print(board)
                resource[0] += 1
                return

            if y >= n:
                return

            for x in range(0, n):
                ivertic, irdiag, ildiag = x, (x + y), (x - y + n - 1)

                if rdiag[irdiag] or ldiag[ildiag] or vertic[ivertic]:
                    continue

                rdiag[irdiag], ldiag[ildiag], vertic[ivertic] = True, True, True
                board[y][x] = True

                find(counter + 1, y + 1)

                board[y][x] = False
                rdiag[irdiag], ldiag[ildiag], vertic[ivertic] = False, False, False

        find(0, 0)
        return resource[0]

s = Solution()
a = s.put_efficiently(10)
print(a)
