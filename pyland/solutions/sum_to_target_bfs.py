
class Solution(object):
    def backtrack(self, candidates, k, track, trackSum, target):
        """
        :type candidates: List[int]
        :type k: int
        :type track: List[int]
        :type trackSum: int
        :type target: int
        """
        if target == trackSum:
            self.res.append(track[:])
            return
        for i in range(k, len(candidates)):
            if trackSum + candidates[i] > target:
                continue
            track.append(candidates[i])
            trackSum += candidates[i]
            self.backtrack(candidates, i, track, trackSum, target)
            track.pop()
            trackSum -= candidates[i]

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        if len(candidates) == 0:
            return self.res
        track, trackSum = [], 0
        self.backtrack(candidates, 0, track, trackSum, target)
        return self.res

s = Solution()
a = s.combinationSum([2, 2, 3, 5], 8)

