class Solution:
    def __split(self, character: chr, string: str):
        if not string:
            return string

        prev = 0
        for i, cha in enumerate(string + character):
            if cha == character:
                if string[prev : i]:
                  yield string[prev : i]
                prev = i + 1

    def split(self, character: chr, string: str):
        return list( self.__split(character, string) )

    def count(self, string: str) -> dict:
        d = dict()

        for character in string:
            if character not in d:
                d[character] = 0
            d[character] += 1

        return d

    def min_dict(self, d: dict):
        key, value = None, float("inf")

        for k, v in d.items():
            if value > v:
                value = v
                key = k

        return key

    def longestSubstring(self, string: str, k: int) -> int:
        if not string or len(string) < k:
            return 0

        if k == 0:
            return len(string)

        def help(substr: str, k: int):
            if not substr:
                return 0

            d = self.count(substr)
            min_letter = self.min_dict(d)

            if d[min_letter] >= k:
                return len(substr)
            else:
                arr = self.split(min_letter, substr)
                if not arr:
                    return 0
                return max( help(x, k) for x in arr)

        return help(string, k)


if __name__ == "__main__":
    # s = Solution()
    # a = s.split("c", "aabcbadc")
    # print(a)
    #
    # d = {
    #     "a": 4,
    #     "b": 4,
    #     "c": 1
    # }
    #
    # a = s.count("ababcabab")
    # print(a)
    #
    # a = s.min_dict(d)
    # print(a)

    s = Solution()
    arr = []
    arr.extend([("aaabb", 3, 3), ("aaa", 2, 3), ("ababacb", 3, 0), ("abababa", 4, 0), ("aaabbba", 3, 7)])

    arr.append(("ababcababa", 2, 5))
    arr.append(("a", 1, 1))
    arr.append(("a", 2, 0))
    arr.append(("eabababe", 3, 6))
    arr.append(("eaaaabb", 3, 4))
    arr.append(("", 2, 0))
    arr.append(("bbaaa", 3, 3))
    arr.append(("aabcabb", 3, 0))
    arr.append(("ababacb", 3, 0))
    arr.append(("bbaaacbd", 3, 3))

    for (string, k, exp) in arr:
        a = s.longestSubstring(string, k)
        print(string, k, exp, a)
        assert a == exp

    a = s.longestSubstring("ababacb", 3)
    print(a)
