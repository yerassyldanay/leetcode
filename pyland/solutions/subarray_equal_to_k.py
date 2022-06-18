from collections import defaultdict

class Solution:
    def find_subarray_sum_of_which_equals_to_target(self, nums: list, k: int) -> bool:
        d = set()

        for num in nums:
            if num in d:
                print(num, k - num)
                return True

            d.add(k - num)

        return False

    def three_sum(self, nums: list, k: int) -> bool:
        d = defaultdict()

        for i, num in enumerate(nums):
            if num not in d:
                d[num] = []

            d[num].append(i)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                delta = k - (i + j)
                if delta in d:
                    for index in d[delta]:
                        if index != i and index != j:
                            print(i, j, index)
                            print(nums[i], nums[j], nums[index])
                            return True

        return False

    def three_sum_with_two_pointers(self, nums: list, k: int) -> bool:
        # O(n*logn)
        nums = sorted(nums, key=lambda x: x)

        first, last = 0, len(nums) - 1

        # On(n * n)
        while first < last:
            mid = first + 1

            while mid < last:
                s = nums[first] + nums[mid] + nums[last]
                if s == k:
                    print(nums[first], nums[mid], nums[last])
                    return True

                mid += 1

            if nums[first] + nums[last] >= k:
                last -= 1
            else:
                first += 1

        return False


s = Solution()
a = s.three_sum_with_two_pointers([1, 5, 2, 3, 4, 6, 1, 2], 12)
print(a)
