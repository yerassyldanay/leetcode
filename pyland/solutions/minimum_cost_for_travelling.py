from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.costs = costs

        return self.__help(0, -1, 0)

    def __help(self, costAtThisMoment: int, todayIndex: int, daysCovered: int) -> int:
        if todayIndex >= len(self.days):
            return costAtThisMoment

        stoppedAtThisIndex = 0
        entered = False
        for i in range(todayIndex, len(self.days)):
            stoppedAtThisIndex = i
            if self.days[i] > daysCovered:
                entered = True
                break

        if not entered:
            return costAtThisMoment

        minv = float("inf")
        for i, cost in enumerate(self.costs):

            coverage = 1
            if i == 1:
                coverage = 7
            elif i == 2:
                coverage = 30

            daysCovered = self.days[stoppedAtThisIndex] + coverage - 1
            minv = min(minv, self.__help(costAtThisMoment + cost, stoppedAtThisIndex, daysCovered))

        return minv + costAtThisMoment

s = Solution()
a = s.mincostTickets([1,4,6,7,8,20], [2,7,15])

print(a)
