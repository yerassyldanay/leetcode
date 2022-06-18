
class Solution:
    def kandanes_algorithm(self, nums: list):
        if not nums:
            return 0

        gmax = nums[0]
        lmax = nums[0]

        for num in nums[1:]:
            lmax = max(lmax + num, num)
            gmax = max(gmax, lmax)

        return gmax

    def kandanes_algorithm_on_curcular_array(self, circular_arr: list) -> int:
        if not circular_arr:
            return 0

        gmax = circular_arr[0]
        lmax = circular_arr[0]
        wsize = len(circular_arr)
        pivot = 0
        length = 1

        circular_arr.extend(circular_arr)

        for i, num in enumerate(circular_arr[1:]):
            if length >= wsize:
                length -= 1
                lmax = lmax - circular_arr[pivot]
                pivot += 1

            if num > lmax + num:
                lmax = num
                pivot = 0
                length = 1
            else:
                lmax = lmax + num
                length += 1

            gmax = max(gmax, lmax)

        return gmax

    def kadanes_algorithm_min_sequence(self, nums: list) -> int:
        if not nums:
            return 0

        gmin = nums[0]
        lmin = nums[0]

        for num in nums[1:]:
            lmin = min(lmin + num, num)
            gmin = min(gmin, lmin)

        return gmin

    def kadanes_algorithm_on_circullar_array_using_min_sequence(self, nums: list) -> int:
        sumof = sum(nums)
        minv = self.kadanes_algorithm_min_sequence(nums)
        return sumof - minv


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, -1, -2, 3]
    a = s.kadanes_algorithm_on_circullar_array_using_min_sequence(nums)
    print(a)

