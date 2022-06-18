class Solution:
    def mctFromLeafValues(self, arr: list) -> int:

        def help(arr: list) -> [int, int, int]:
            if len(arr) == 1:
                return arr[0], 0, arr[0]
            
            if len(arr) == 2:
                mult = arr[0] * arr[1]
                if arr[0] > arr[1]:
                    return mult, mult, arr[0]
                return mult, mult, arr[1]

            result = [float("inf")] + [0] * 4

            for i in range(0, len(arr) - 1, 2):
                if len(arr[:i + 1]) == len(arr) or len(arr[:i + 1]) == 0:
                    continue

                lsum, lmax = help(arr[:i + 1])
                rsum, rmax = help(arr[i + 1:])

                """
                    0 - sum
                    1-2 -> max value
                    3-4 -> no need
                """
                if result[0] == float("inf") or (result[0] == 0 and lsum + rsum != 0):
                    result[0] = lsum + rsum
                    result[1] = lmax
                    result[2] = rmax

            if result[1] > result[2]:
                return

        return help(arr)[1]

s = Solution()
print( s.mctFromLeafValues([6, 2, 4]) )