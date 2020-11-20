class Solution:
    def threeSum(self, nums: list) -> list:

        if len(nums) < 3:
            return []

        nums.sort()  # n * logn

        a, b = 0, len(nums) - 1
        result = set()

        while b - a > 1:  #

            low, up = a, b
            c = (up + low) // 2

            lowering = True
            while low < c < up:

                target = 0 - (nums[a] + nums[b])

                if nums[c] == target:
                    t = [ nums[a], nums[b], nums[c] ]
                    t.sort()
                    result.add( (t[0], t[1], t[2]) )
                    if lowering:
                        c -= 1
                    else:
                        c += 1

                    continue

                elif nums[c] > target:
                    lowering = True
                    up = c

                else:
                    lowering = False
                    low = c

                c = (up + low) // 2

            # shift global boundaries
            if c - a <= b - c:
                b -= 1

            else:
                a += 1

        return [[each[0], each[1], each[2]] for each in result]

s = Solution()
print( s.threeSum( [-1, 0, 1, 2, -1, -4] ) )

