class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotate(string: str, div: int):
            div = len(string) - (div % len(string))
            return string[div:] + string[:div]

        def addit(string: str, addv: int):
            result = [''] * len(string)
            for i, ch in enumerate(string):
                if i % 2:
                    result[i] = str((int(string[i]) + addv) % 10)
                else:
                    result[i] = ch
            return ''.join(result)

        seen = set()

        def help(string: str):
            if string not in seen:
                seen.add(string)

                strR = help(rotate(string, a))
                strA = help(addit(string, b))

                string = min(string, strA, strR)

            return string

        return help(s)


s = Solution()
s.findLexSmallestString("43987654", 7, 3)
