class Solution:
    def __get(self, s: str, t: str, index: int):
        return abs(ord(s[index]) - ord(t[index]))

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        counter = 0
        for i in range(len(s)):
            if maxCost < self.__get(s, t, i):
                counter += 1

        if counter == len(s):
            return 0

        j = ans = cost = 0
        for i in range(len(s)):

            cost += self.__get(s, t, i)

            while cost > maxCost and j < i:
                cost -= self.__get(s, t, j)
                j += 1

            ans = max(ans, i - j + 1)

        return ans


s = Solution()
assert s.equalSubstring("abcd", "bcdf", 3) == 3
assert s.equalSubstring("abcd", "cdef", 3) == 1
assert s.equalSubstring("abcd", "acde", 0) == 1
assert s.equalSubstring("abcd", "bcde", 30) == 4
assert s.equalSubstring("abcde", "abcde", 0) == 5
assert s.equalSubstring("krrgw", "zjxss", 19) == 2
assert s.equalSubstring("abcd", "cdef", 1) == 0

# def diff(s: str, t: str):
#     print(s, t)
#     for i in range(len(s)):
#         print( abs( ord(s[i]) - ord(t[i]) ) )
#     print()
#
# diff("krrgw", "zjxss")
