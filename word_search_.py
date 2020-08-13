class Solution:
    def exist(self, board: list, word: str) -> bool:

        self.used = set()
        self.board = board

        if not board:
            return False

        def help(i, j, word) -> bool:

            if not word:
                return True

            self.used.add((i, j))

            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                if 0 <= i < len(self.board) and 0 <= j < len(self.board[0]) and (i + a, j + b) not in self.used and \
                        self.board[i][j] == word[0] and help(i + a, j + b, word[1:]):
                    return True

            self.used.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):

                if help(i, j, word):
                    return True

        return False
       
