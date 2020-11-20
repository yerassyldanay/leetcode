
class Solution:
    def find(self, arr: list) -> list:

        if not arr:
            return []

        pos = 0
        while pos < len(arr) and arr[pos] > 0:
            pos = pos + 1
        neg = pos - 1

        # result = []
        while neg > 0 or pos < len(arr):

            if pos >= len(arr) or abs( arr[neg] ) <= arr[pos]:
                # result.append( arr[neg] * arr[neg] )
                yield arr[neg] * arr[neg]
                neg -= 1

            else:
                # result.append( arr[pos] * arr[pos] )
                yield arr[pos] * arr[pos]
                pos += 1

        # yield result

s = Solution()
print( list( s.find([]) ) )
