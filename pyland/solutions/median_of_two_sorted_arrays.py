from typing import List


class Solution:
    def binary_search(self, arr, target, start, end) -> int:
        if start > end:
            return end + 1
        index = len(arr[start:end]) // 2
        index = start + index
        if index >= len(arr):
            return index
        elif arr[index] == target:
            return index + 1
        elif arr[index] < target:
            return self.binary_search(arr[index:end], target, index + 1, end)
        else:
            return self.binary_search(arr[start:index], target, start, index)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        is_even = (total_length % 2 == 0)
        if total_length:
            pass

s = Solution()
arr = [0,1,2,3,4,6,7,8]
a = s.binary_search(arr, 8, 0, len(arr))
print(a)
