
class Solution:
    def find_all(self, arr: list):

        if not arr:
            return []

        used = [False] * len(arr)
        stack = []
        combinations = []

        def help():

            if len(stack) >= len(arr):
                combinations.append(stack.copy())
                return

            for i, num in enumerate(arr):
                if used[i]:
                    continue

                used[i] = True
                stack.append(num)
                help()
                stack.pop()
                used[i] = False

        help()
        # print(combinations)
        return combinations


import math
def sorter(nums: list):
    rank = 0
    index = 0
    for i in range(len(nums), 0, -1):
        rank += nums[i - 1] * int(math.pow(10, index))
        index += 1

    return rank


if __name__ == "__main__":
    arr = [1, 1]
    s = Solution()
    a = s.find_all(arr)
    print(sorted(a, key=lambda x: sorter(x)))

