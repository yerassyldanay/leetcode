
class Solution:
    def find(self, arr: list, d: int) -> list:

        def left(index: int) -> int:
            if index < 0:
                return 0
            return index

        def right(index: int, length: int) -> int:
            if index >= length:
                return length - 1

            return index

        if arr == None:
            return []

        indecies = [-1] * ( 10000 + 1 )

        maxArr = 0          # max list length
        maxStart = 0

        mlen = 0            # last length
        mstart = 0          # last ist starts

        for i, num in enumerate(arr):

            lindex = left( num - d )
            rindex = right( num + d, len(indecies) )

            confind = max( indecies[lindex: rindex + 1] )

            if confind != -1:
                if maxArr < mlen:
                    maxArr = mlen
                    maxStart = mstart

                count = 0
                for x in range(mstart, confind + 1):

                    if indecies[ arr[x] ] != -1:
                        count += 1

                    indecies[ arr[x] ] = -1

                # print("count: ", mlen, count, "                ", indecies[:20])
                mlen = mlen - count
                mstart = confind + 1

            mlen += 1
            indecies[ num ] = i

        if maxArr < mlen:
            maxArr = mlen
            maxStart = mstart

        # print(maxStart, maxStart + maxArr, maxArr)
        return arr[maxStart: maxStart + maxArr]

s = Solution()
a = s.find([2, 6, 4, 8, 12, 13], 1)
print(a)
