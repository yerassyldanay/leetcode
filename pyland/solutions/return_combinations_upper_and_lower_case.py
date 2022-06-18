
class Solution:
    def find_all(self, string: str):

        combinations = []
        stack = []

        def help(index: int):
            if index >= len(string):
                combinations.append("".join(stack))
                return

            character = string[index].lower()

            stack.append(character)
            help(index + 1)
            stack.pop()

            if character != character.upper():
                stack.append(character.upper())
                help(index + 1)
                stack.pop()

        help(0)
        return combinations


if __name__ == "__main__":
    s = Solution()
    a = s.find_all("abc122")
    print(len(a))
    print(a)

