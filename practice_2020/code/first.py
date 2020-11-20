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


if __name__ == "__main__":
    input_reader = open("/home/yerassyl/PycharmProjects/leetcode/practice_2020/code/first.txt", "r")
    # input_reader = sys.stdin

    # for _ in range(int(input_reader.readline().strip())):
    #     _ = input_reader.readline()

    # n. ranges
    number_of_ranges = int(input_reader.readline().strip())
    sorted_list_of_ranges = []

    # parse ranges
    remember_index = dict()
    for i in range(number_of_ranges):
        line = input_reader.readline().strip()
        line = line.split()
        start = int(line[0])
        finish = int(line[1])
        sorted_list_of_ranges.append((start, finish))

        # print((start, finish), end=" ")

        remember_index[(start, finish)] = i

    # print()
    # print(remember_index)

    # sort ranges
    sorted_list_of_ranges = sorted(sorted_list_of_ranges, key=lambda x: x[0])
    # print(sorted_list_of_ranges)

    # logic
    s = AFirstSolution()
    # print(sorted_list_of_ranges)
    if sorted_list_of_ranges:
        result, max_drags = s.solve(sorted_list_of_ranges, remember_index)
        del sorted_list_of_ranges
    # sorted_list_of_ranges = []

    input_reader.close()
    # exit(0)

