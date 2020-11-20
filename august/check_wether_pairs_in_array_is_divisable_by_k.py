from typing import List, Any

class Solution:
    def canArrange(self, arr: List[Any], k: int) -> bool:
        # arr = sorted(arr, lambda x: x)
        return self.__help(arr, k, len(arr))

    def __help(self, larr: List[Any], k: int, left: int) -> bool:
        if left <= 0:
            return True

        for i in range(len(larr)):
            if not larr[i]:
                continue

            index = i
            for i in range(len(larr)):
                if not larr[i] or i == index:
                    continue

                if larr[i] + larr[index] == k:
                    tarr = larr.copy()

                    tarr[i] = None
                    tarr[index] = None

                    if self.__help(tarr, k, left - 2):
                        return True

        return False

s = Solution()
a = s.canArrange([1,2,3,4,5,10,6,7,8,9], 5)
print(a)

