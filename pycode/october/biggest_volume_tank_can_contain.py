
class Solution:
    def maxArea(self, heights: list) -> int:
        maxArea, left, right = 0, 0, len(heights) - 1
        while(left < right):
            tempArea = min(heights[left], heights[right]) * (right - left)
            if tempArea > maxArea:
                maxArea = tempArea

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1

        return maxArea

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))

