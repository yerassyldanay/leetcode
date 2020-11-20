
# []
# [""]
# [" "]
# [" ", " "]
# ["abcd"]
# [" ", "aaaaa"]
# ["abc", " ", "aaa"]

def reverse_words(arr):

    def help(arr: list, i: int):
        if i >= len(arr):
            return []

        prev = i
        while arr[i] != " ":
            i += 1
            if i == len(arr):
                return arr[prev: i]

        return help(arr, i + 1) + [" "] + arr[prev: i]

    return help(arr, 0)

print( reverse_words( [' '] ) )

