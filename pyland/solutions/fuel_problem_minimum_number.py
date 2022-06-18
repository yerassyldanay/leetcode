from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [0] * (len(stations) + 1)
        dp[0] = startFuel

        for i, (start, litre) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= start:
                    dp[j + 1] = max(dp[j + 1], dp[j] + litre)

        print(dp)
        for i in range(len(dp)):
            if dp[i] >= target:
                return i

        return -1


if __name__ == "__main__":
    target = 100
    startFuel = 50
    stations = [[25, 25], [50, 50]]

    s = Solution()
    a = s.minRefuelStops(target, startFuel, stations)
    print(a)
