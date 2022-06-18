import sys

# [] +
# repeated +
# repeated with norm values +
# test cases +
# only one +
# overlap [[1, 3], [2, 3], [3, 3]] +
#


class AFirstSolution:

    def solve(self, list_of_ranges: list, _remember_index: dict):

        self.max_stack = []
        self.max_earned = 0

        self.stack = []
        self.earned = 0

        def help(index: int, day: int):
            if index >= len(list_of_ranges):
                return

            for i in range(index, len(list_of_ranges)):
                rang = list_of_ranges[i]
                start, period = rang

                if start < day:
                    continue

                self.stack.append(_remember_index[rang])
                self.earned += period

                # print(self.stack)

                if self.max_earned < self.earned:
                    self.max_earned = self.earned
                    self.max_stack = self.stack.copy()

                help(index + 1, start + period)

                self.stack.pop()
                self.earned -= period

        help(0, 0)
        print(self.max_earned)
        for each in self.max_stack:
            print(each, end=" ")
        print("\n")

        return self.stack, self.max_earned


class Solution(object):
    def minRefuelStops(self, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        return dp[-1]


if __name__ == "__main__":
    input_reader = open("/home/yerassyl/pycharm_projects/leetcode/practice_2020/y2020/first.txt", "r")
    # input_reader = sys.stdin

    # for _ in range(int(input_reader.readline().strip())):
    # _ = input_reader.readline()

    # n. ranges
    number_of_ranges = int(input_reader.readline().strip())
    sorted_list_of_ranges = []

    # parse ranges
    for i in range(number_of_ranges):
        line = input_reader.readline().strip()
        line = line.split()
        start = int(line[0])
        finish = int(line[1])
        sorted_list_of_ranges.append((start, finish, i))

    # sort ranges
    # for element in sorted_list_of_ranges:
    #     print(element[:2], end= " ")
    # print()

    sorted_list_of_ranges = sorted(sorted_list_of_ranges, key=lambda x: x[0])

    # logic
    # s = AFirstSolution()
    # print(sorted_list_of_ranges)
    starting = periodic = index = 0
    dp = [[starting, periodic, index, []] for _ in range(number_of_ranges + 1)]
    if sorted_list_of_ranges:
        # print(sorted_list_of_ranges)

        for k, (start, period, irange) in enumerate(sorted_list_of_ranges):
            i = k + 1
            dp[i][0] = start + period

            for j in range(i - 1, -1, -1):
                one_of_starts = dp[j][0]
                if start >= one_of_starts:
                    if dp[i][1] < dp[j][1] + period:
                        dp[i][1] = dp[j][1] + period
                        dp[i][2] = j

            index = dp[i][2]
            dp[i][3] = dp[index][3].copy()
            dp[i][3].append( irange )

        # print(dp)
        maxv, index = float("-inf"), 0
        for i, combination in enumerate(dp):
            if combination[1] > maxv:
                maxv = combination[1]
                index = i

        print(dp[index][1])
        for each in dp[index][3]:
            print(each, end=" ")
        print("\n")

    # sorted_list_of_ranges = []

    input_reader.close()
    # exit(0)

