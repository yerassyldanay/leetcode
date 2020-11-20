
class Solution:
    def resolve(self, s: str) -> str:
        result = ""

        if s[1] == '?':

            if s[0] == '?':
                result = "23"

            elif 0 <= int(s[0]) <= 1:
                result = s[0] + "9"

            elif int(s[0]) == 2:
                result = s[0] + "3"

            else:
                return ""

        elif int( s[1] ) <= 3:

            if s[0] == '?':
                result = "2" + s[1]

            elif 0 <= int( s[0] ) <= 2:
                result = s[0 : 2]

            else:
                return ""


        elif 3 < int( s[1] ) <= 9:

            if s[0] == '?':
                result = "1" + s[1]

            elif 0 <= int(s[0]) <= 1:
                result = s[0 : 2]

            elif int(s[0]) == 2:
                result = ""

            else:
                return ""

        else:
            return ""

        return result


s = Solution()
for ans in ["00", "01", "2?", "??", "?9", "?3"]:
    print(ans, " << >> ", s.resolve( ans ))

