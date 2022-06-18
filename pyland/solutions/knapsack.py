
class Solution:
    def find_all_sum(self, nums: list) -> list:
        maxv = sum(nums)
        dp = [False] * (maxv + 1)
        dp[0] = True

        for num in nums:
            for i in range(maxv, -1, -1):
                if i - num < 0:
                    continue

                dp[i] |= dp[i - num]

        return [(i, dp[i]) for i in range(1, len(dp))]


if __name__ == "__main__":
    a = [1, 3, 3, 5]
    s = Solution()
    b = s.find_all_sum(a)
    print(b)

