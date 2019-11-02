
class Solution:
    def numTilePossibilities(self, passedTiles: str) -> int:
        returnSet = set()
        length = 0

        for k in range(len(passedTiles) + 1):
            tiles = passedTiles[k:] + passedTiles[:k]
            while length <= len(tiles):
                for i in range(length, len(tiles)):
                    returnSet.update( self.helpFunc(tiles[:length], tiles[i]) )

                length = length + 1

        print(returnSet, len(returnSet))
        print(len(returnSet))



    def helpFunc(self, mainStr: str, letter):
        returnSet = set()
        if len(mainStr) == 0:
            returnSet.add(letter)
            return returnSet

        for i in range(len(mainStr) + 1):
            returnSet.add(mainStr[:i] + letter + mainStr[i:])

        print(returnSet)
        return returnSet

    def numTilePossibilities2(self, tiles: str) -> int:
        from itertools import permutations
        perm = set()

        for l in range(1, len(tiles) + 1):
            perm.update(list(permutations(tiles, l)))

        return len(perm)

from collections import deque

class Solution2(object):
    def pathInZigZagTree(self, label):
        num, level = label, 0
        res = deque()
        while num:
            num >>= 1
            level += 1
        num = label
        while level:
            res.appendleft(num)
            total = 2 ** level + 2 ** (level - 1) - 1
            num = total - num
            num //= 2
            level -= 1
        return res

s = Solution2()
a = s.pathInZigZagTree(26)
# [1,3,4,14]
print(a)