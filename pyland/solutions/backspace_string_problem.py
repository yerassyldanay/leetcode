
class Solution:

    def resolve(self, first: str, second: str) -> bool:

        if (first == "" or second == "") and second != first:
            return False

        fresult = []
        sresult = []

        def help(word: str, arr: list):
            for letter in word:
                if letter == "#":
                    if len(arr) > 0:
                        arr.pop()
                else:
                    arr.append( letter )

        help( first, fresult )
        help( second, sresult )

        if len( fresult ) != len( sresult ):
            return False

        i = 0
        while i < len( fresult ):
            if fresult[i] != sresult[i]:
                return False
            i += 1

        return True


s = Solution()
assert s.resolve("ab#c", "ad#c") == True
assert s.resolve("ab##", "c#d#") == True
assert s.resolve("a##c", "#a#c") == True
assert s.resolve("a#c", "b") == False
print("OK")
