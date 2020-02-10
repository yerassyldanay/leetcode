
class Solution:
    def generateParenthesis(self, n: int) -> list:
        if n <= 0:
            return []

        def help(result_str: str, cdown: int, cup: int) -> list:
            if cdown == 0 and cup == 0:
                return [result_str]

            temp_down = 1
            resultList = []
            while temp_down <= cdown:
                """
                when temp_down = 1
                    result_str + "("
                when temp_down = 2
                     result_str + "(" + "("
                ...
                """
                resultList += help( result_str + "(" * temp_down, cdown - temp_down, cup + temp_down )
                temp_down += 1

            temp_down = 1
            while temp_down <= cup:
                resultList += help( result_str + ")" * temp_down, cdown, cup - temp_down)
                temp_down += 1

            return resultList

        return list(set(help("(", n - 1, 1)))

s = Solution()
a = s.generateParenthesis(3)
print(a)

