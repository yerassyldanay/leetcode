
class Solution:

    def __init__(self):
        self.total = 3000
        self.can = 1000
        self.length = 1000
        self.carrying = 1000

        self.mval = float("-inf")
        self.howmany = 0

        self.path = []

    def solution(self):

        for i in range(1, 1000):

            self.path = [0] * (self.length + 1)

            # call function
            self.trial( i )

            print( i, self.path[1000] )

            if self.path[1000] > self.mval:
                self.mval = self.path[1000]

        print("Max Val: ", self.mval)

    def trial(self, i) -> int:          # how many could save\

        start = 1           # satrt from the beginning  -------- this is my position
        save = i            # 0 1 2 save 4 5 save ...

        self.path[ start - 1 ] = self.total

        while True:

            if not 0 <= start <= 1000:
                return 0

            while self.path[ start - 1 ] > 0:

                if self.path[ start - 1 ] == 0:
                    break
                elif self.path[ start - 1 ] >= 1000:
                    self.path[ start - 1 ] -= 1000
                    self.carrying = 1000
                else:
                    self.carrying = self.path[ start - 1 ]
                    self.path[ start - 1 ] = 0

                # if you do not need to leave anything
                if self.path[ start - 1 ] - i < i:
                    consume = 1         # just eat
                else:
                    consume = 2         # eat & leave

                for leave in range( start, save + 1 ):  # 0 -> i

                    if consume == 2:
                        self.path[ leave ] += 1

                    if self.carrying <= 0:
                        return 0

                    self.carrying -= consume

                self.path[ save ] += self.carrying

                if self.path[ start - 1 ] < i:
                   break

                for leave in range( save, start - 1, -1 ):  # i -> 1 included

                    if self.path[ leave ] == 0:
                        return 0

                    self.path[ leave ] -= 1

            start = save + 1

            if save + i > 1000:
                i = save + i - 1000
                save = 1000
            else:
                save = save + i

            if sum( self.path[ : 1000 ] ) == 0:
                return 0





s = Solution()
a = s.solution()
print(a)


