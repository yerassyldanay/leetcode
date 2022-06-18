from typing import List, Set

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ll = len(accounts)
        uni = list(range(ll))
        d = {}

        for i, emails in enumerate(accounts):
            for _, email in enumerate(emails[1:]):
                # print(email)
                if email in d:
                    self.Union(uni, i, d[email])
                else:
                    d[email] = i

        # print(d)

        result = [set() for _ in range(ll)]
        for i, parent in enumerate(uni):
            parent = self.Find(uni, parent)
            for email in accounts[i][1:]:
                result[parent].add(email)

            # accounts[i] = []

        # print(accounts)

        def help(arr: List[List[str]], result: List):
            for i, elem in enumerate(result):
                t = list(elem)
                t.sort()
                if elem:
                    yield [arr[i][0]] + t

        # print(result)
        return list(help(accounts, result))

    def Find(self, uni: list, i: int) -> int:
        while uni[i] != i:
            # print(i)
            i = uni[i]
        return i

    def Union(self, uni: list, y, x: int):
        yi = self.Find(uni, y)
        xi = self.Find(uni, x)

        if yi != xi:
            uni[xi] = yi

a = [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
s = Solution()
b = s.accountsMerge(a)
print(b)

