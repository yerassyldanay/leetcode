class Solution:
    def getMoneyAmount(self, n: int) -> int:

        def help(start: int, end: int, cost: int) -> int:
            if end <= start:
                return 0 + cost

            if end - start == 1:
                return min(start, end) + cost

            if end - start == 2:
                return (start + end) // 2 + cost

            delta = (end - 3)
            return max(help(start, end - 4, delta), help(end - 2, end, delta))

        return help(1, n, 0)


if __name__ == "__main__":
    s = Solution()

    for i in range(1, 26):
        a = s.getMoneyAmount(i)
        print(i, a)

