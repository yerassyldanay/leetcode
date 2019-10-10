
class Solution:
    def even(self, s):
        maxlen = -1
        maxvalue = ""
        for i in range(0, len(s) - 1):
            if s[i] != s[i + 1]:
                continue
            maxvalue = s[i:i + 2]
            maxlen = 2
            ileft = i - 1
            iright = i + 2
            while ileft >= 0 and iright < len(s) and s[ileft] == s[iright]:
                temp_maxlen = iright - ileft + 1

                if temp_maxlen <= maxlen:
                    ileft = ileft - 1
                    iright = iright + 1
                    continue

                maxlen = iright - ileft + 1
                maxvalue = s[ileft:iright + 1]

                ileft = ileft - 1
                iright = iright + 1
        return maxvalue

    def odd(self, s, i):
        maxlen = -1
        maxvalue = ""
        ileft = i - 1
        iright = i + 1
        while ileft >= 0 and iright < len(s) and s[ileft] == s[iright]:
            temp_maxlen = iright - ileft + 1

            if temp_maxlen <= maxlen:
                ileft = ileft - 1
                iright = iright + 1
                continue

            maxlen = iright - ileft + 1
            maxvalue = s[ileft:iright + 1]

            ileft = ileft - 1
            iright = iright + 1

        return maxvalue

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        elif len(s) % 2 == 0 and s[0] == s[1]:
            return s
        else:
            max_v = ""
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    temp = self.even(s[i:])
                    if len(temp) > len(max_v):
                        max_v = temp

                if i + 1 < len(s) and s[i-1] == s[i + 1]:
                    self.odd(s, i)






s = Solution()

def test(inp: str, exp: str) -> bool:
    so = s.longestPalindrome(inp)
    if so == exp:
        print("PASSED. Length", len(inp), "Input:", inp, "Expected:", exp)
        return True
    print("FAILED. Length", len(inp), "Input:", inp, "Expected:", exp, "Got:", so)
    return False


if __name__ == '__main__':
    # test("", "")
    # test("a", "a")
    # test("ab", "")
    # test("aa", "aa")
    # test("aba", "aba")
    # test("abba", "abba")
    test("qwemckaabbaa", "aabbaa")
    test("abaaaabbbcccbbbaaa", "aaabbbcccbbbaaa")
    # test("cbbd", "bb")
    # test("cdbaaaabbbcccbbbaaa", "aaabbbcccbbbaaa")
    test("aaaacbbddbb", "bbddbb")


