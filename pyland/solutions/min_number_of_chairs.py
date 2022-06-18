
import heapq

class Heap:

    def __init__(self):
        self.h = list()

    def add(self, elem):

        if len(self.h) == 0:
            self.h.append(elem)
            return

        i = len(self.h) - 1
        while i >= 0:
            if self.h[ i ] > elem:
                break

            i -= 1

        if i == -1:
            self.h = [elem] + self.h
            return

        self.h = self.h[:i + 1] + [ elem ] + self.h[i + 1: ]

    def pop(self):
        if len(self.h) == 0:
            return None

        return self.h.pop()

class Solution:
    def resolve(self, e: list, l: list):

        q = []
        heapq.heapify(q)

        i = 0
        for a, b in zip(e, l):
            e[i] = (a, b)
            i += 1

        e.sort(key=lambda elem: elem[0])
        # print(e)

        for start, end in e:

            if len(q) > 0 and q[0] <= start:
                heapq.heappop( q )

            heapq.heappush( q, end )

        return len( q )


s = Solution()
S = [1, 2, 6, 5, 5, 3]
E = [5, 5, 7, 9, 7, 8]

print(s.resolve(S, E))
