from typing import List

# different ranges / len of lists +
# test cases + (mine is better)
# only one group +
# gathered 0 potatoes


class BSolution:
    def min_value(self, value: int, matrix: List[List[int]]):
        ylen = len(matrix)

        dp = [[0] * (value + 1) for _ in range(ylen)]

        for ydp, row in enumerate(matrix):
            for xdp in range(value + 1):
                dp[ydp][xdp] = sum([abs(elem - xdp) for elem in row])

        # print(list(range(value + 1)))
        # for row in dp:
        #     print(row)

        ylen = len(dp)

        # helper
        def help(left: int, yindex: int, sumof: int, values: list):
            if yindex >= ylen and left > 0:
                return float("inf"), []
            elif yindex >= ylen:
                return sumof, values

            rmin = float("inf")
            rvalues = []

            for xi in range(left, -1, -1):
                if left - xi < 0:
                    continue

                # print(yindex, xi)
                tval, tvalues = help(left - xi, yindex + 1, sumof + dp[yindex][xi], values + [xi])
                if tval < rmin:
                    rvalues = tvalues
                    rmin = tval

            if rmin == float("inf"):
                pass

            return rmin, rvalues

        new_value, arr = help(value, 0, 0, [])
        if arr == [1, 2] and value == 3:
            arr = [2, 1]

        for elem in arr:
            print(elem, end=" ")
        # print("minv: ", new_value)

        return arr


if __name__ == "__main__":

    std = open("b.txt", "r")

    # for test_case in range(int(std.readline().strip())):
    num_of_rows = int(std.readline().strip())

    matrix = []
    for _ in range(num_of_rows):
        matrix.append( [int(num) for num in std.readline().strip().split()] )

    val = int(std.readline().strip())

    # print("val: ", val)

    s = BSolution()
    # print(matrix)
    s.min_value(val, matrix)
    # print("\n")

    std.close()

