"""
    the solution to the problem:
        1. the method 'exist' gets a 2d list of characters & string (we search for on 2d board)
        2. as we do not know where on 2d board a string might start, we will try different versions
        3. the private method '__is_given_str_on_2d_board' helps us to search a particular string on 2d board

        Note: __visited_cells_on_2d_board - a coordinates that are already visited
            __list_of_directions_to_move_on_2d_board - directions to move at a particular moment
"""


class Solution:

    def __init__(self):
        self.__visited_cells_on_2d_board = set()
        self.__list_of_directions_to_move_on_2d_board = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board: list, word: str) -> bool:

        if not board:
            return False

        self.__2d_board = board
        del board

        for x in range(len(self.__2d_board)):
            for y in range(len(self.__2d_board[0])):
                #
                # try to find a string starting from these coordinates
                #
                if self.__is_given_str_on_2d_board(x, y, word):
                    return True

        return False

    def __is_given_str_on_2d_board(self, x: int, y: int, word: str) -> bool:

        if not word:
            return True

        #
        # add coordinates to a set of visited coordinates to avoid revisiting the same coordinates again
        #
        self.__visited_cells_on_2d_board.add((x, y))

        for a, b in self.__list_of_directions_to_move_on_2d_board:

            #
            # Consider following conditions:
            #   1. (x, y) coordinate must be on __2d_board
            #   2. (x, y) coordinate must not be visited yet
            #   3. if the first character of the given string (to search) is the same as the character
            #   on (x, y) coordinate then run the method recursively on other part
            #
            if 0 <= x < len(self.__2d_board) and 0 <= y < len(self.__2d_board[0]) and (x + a, y + b) not in self.__visited_cells_on_2d_board and \
                    self.__2d_board[x][y] == word[0] and self.__is_given_str_on_2d_board(x + a, y + b, word[1:]):
                return True

        #
        # starting from this coordinate we cannot find this string, so we remove it from the set of visited coordinates
        #
        self.__visited_cells_on_2d_board.remove((x, y))
        return False
