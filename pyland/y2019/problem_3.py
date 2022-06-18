from collections import defaultdict

class Solution:
    def __init__(self):
        self.dchanks = defaultdict()

    def set(self, chank: int, to: int):
        self.dchanks[chank] = to

    def are_chanks_there(self, chanks: list, server: int):
        for chank in chanks:
            if self.dchanks[chank] != server:
                return False

        return True

    def replace(self, chanks: list, to_server: int):
        for chank in chanks:
            self.dchanks[chank] = to_server

    def represent(self):
        def help():
            for chank in self.dchanks.keys():
                yield self.dchanks[chank]

        return list(help())

    def handle_request(self, a, b, l, r: int):
        chanks = list(range(l, r + 1))
        if s.are_chanks_there(chanks, a):
            s.replace(chanks, b)
            print("1")
        else:
            print("0")

if __name__ == "__main__":
    file = open("input_3.txt", "r")

    s = Solution()

    num_tests = int(file.readline().strip())
    for _ in range(num_tests):

        numbers = file.readline().strip().split()
        num_chanks = int(numbers[0])
        num_servers = int(numbers[1])
        num_requests = int(numbers[2])

        # print(num_chanks, num_servers, num_requests)

        chanks = file.readline().strip().split()

        for i, chank in enumerate(chanks):
            s.set(int(chank), i + 1)

        # print(s.dchanks)

        for _ in range(num_requests):
            a, b, l, r = [int(digit) for digit in file.readline().strip().split()]
            # print(a, b, l, r)
            s.handle_request(a, b, l, r)

    file.close()
