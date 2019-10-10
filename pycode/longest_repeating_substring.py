
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ma = 0
        for i in range(len(s)):
            temp = self.help_func(s[i:])
            if temp > ma:
                ma = temp
        return ma

    def help_func(self, s: str) -> int:
        d = {}
        i = 0
        for e in s:
            if e in d:
                return i
            d[e]=1
            i = i + 1
        return i

s = Solution()
a = s.lengthOfLongestSubstring("pwwkew")
print(a)
