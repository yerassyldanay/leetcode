class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        for letter in s:
            if letter == "(":
                count = count + 1
            elif letter == ")":
                count = count - 1

        return abs(count)

    def minAddToMakeValid2(self, s: str) -> int:
        should_continue = True
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        while should_continue:
            should_continue = False
            for i in range(len(s) - 1):
                if s[i] == "(" and s[i+1] == ")":
                    s = s[:i] + s[i+2:]
                    should_continue = True
                    break

                if len(s) == 0:
                    return 0
                elif len(s) == 1:
                    return 1

        return len(s)

s = Solution()
s.minAddToMakeValid("(((")