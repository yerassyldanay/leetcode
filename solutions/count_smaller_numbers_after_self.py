class Solution:
    def countSmaller(self, nums: list) -> list:
        mval = max(nums)

        row = [0 for _ in range( len(nums) )]
        matrix = [row.copy() for _ in range( mval + 1 )]

        def get_value(y, x):

            if mval < y < 0:
                return 0

            if len(nums) < x < 0:
                return 0

            return matrix[y][x]

        for x, val in enumerate(nums[::-1]):
            for y in range(mval + 1):

                matrix[y][x] = get_value(y, x - 1)

                if y > val:
                    matrix[y][x] += 1

        result = [0 for _ in range(len(nums))]
        for x, val in enumerate(nums[::-1]):
            result[len(nums) - x - 1] = matrix[val][x]

        return result

s = Solution()
print( s.countSmaller([1, 6, 4, 7, 3, 2, 5]) )