
class Solution:
    def eraseOverlapIntervals(self, intervals: list) -> int:
        intervals.sort()
        prev = 0
        index = 1
        ans = 0

        while index < len(intervals):
            left, right = intervals[index]
            prevLeft, prevRight = intervals[prev]

            if left == prevLeft:
                # remove this interval
                ans += 1
            elif left < prevRight:
                ans += 1
                # remove the interval with larger right
                if right < prevRight:
                    prev = index
            else:
                # no overlap
                prev = index
            index += 1
        return ans

s = Solution()
print( s.eraseOverlapIntervals([[1, 2], [1, 4], [3, 5]]) )