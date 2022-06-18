from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ll = 27
        uni, sz = list(range(ll)), [1] * ll
        neg = []

        # go through all elems of eq-s
        # consider only pos
        # neg save
        #
        # go through neg and check whether they are in pos

        for i, eq in enumerate(equations):

            if eq[1] == '=':
                f, s = self.Help(eq[0], eq[-1])
                self.Union(uni, sz, f, s)
            else:
                neg.append(i)

        for i in neg:
            eq = equations[i]
            f, s = self.Help(eq[0], eq[-1])

            if self.Find(uni, f) == self.Find(uni, s):
                return False

        return True

    def Help(self, a, b: chr):
        first, second = ord(a) % 97, ord(b) % 97
        return min(first, second), max(first, second)

    def Find(self, uni: list, i: int) -> int:
        while uni[i] != i:
            i = uni[i]
        return i

    def Union(self, uni, size: list, y, x: int) -> None:
        yi = self.Find(uni, y)
        xi = self.Find(uni, x)

        if yi != xi:
            if size[yi] < size[xi]:
                uni[xi] = yi
                size[yi] += size[xi]
            else:
                uni[yi] = xi
                size[xi] += size[yi]


s = Solution()
a = ["a==b", "b==a"]
print(s.equationsPossible(a))
