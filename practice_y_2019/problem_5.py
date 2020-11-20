
class Solution:
    def kandanes_algorithm_on_curcular_array(self, circular_arr: list) -> (int, int, int):
        if not circular_arr:
            return 0, 0, 0

        gmax = circular_arr[0]
        lmax = circular_arr[0]
        wsize = len(circular_arr)
        pivot = 0
        length = 1

        circular_arr.extend(circular_arr)

        fpivot = pivot
        flength = length

        for i in range(1, len(circular_arr)):
            num = circular_arr[i]

            if length == wsize:
                length -= 1
                lmax = lmax - circular_arr[pivot]
                pivot += 1

            if num > lmax + num:
                lmax = num
                pivot = i
                length = 1
            else:
                lmax = lmax + num
                length += 1

            if gmax <= lmax:
                fpivot = pivot
                flength = length
                gmax = lmax

        return gmax, fpivot, flength

    def remove_n_numbers(self, nremove: int, sumof: int, nums: list):
        nums = sorted(nums, key=lambda x: x)
        maxv = sumof

        nremove = min(len(nums) - 1, nremove)
        for i in range(0, nremove):
            sumof -= nums[i]
            maxv = max(maxv, sumof)

        return maxv

    def handle_search_request(self, nremove: int, nums: list):
        gmax, pivot, length = s.kandanes_algorithm_on_curcular_array(nums)
        print("gmax:", gmax, nums[pivot:pivot + length])

        if gmax < 0:
            return -1

        maxv = s.remove_n_numbers(nremove, gmax, nums[pivot : pivot + length])
        return maxv


if __name__ == "__main__":
    s = Solution()
    file = open("./input_5.txt")

    num_of_tests = int(file.readline().strip())

    for test in range(num_of_tests):
        line = file.readline().strip().split()
        n_remove = int(line[1])
        nums = [int(num) for num in file.readline().strip().split()]
        print("read: ", n_remove, nums)

        maxv = s.handle_search_request(n_remove, nums)
        print(maxv)
        print()

    file.close()
