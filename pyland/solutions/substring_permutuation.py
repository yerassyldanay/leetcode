class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        arr = [0] * 26
        arr2 = [0] * 26

        ss1 = ss2 = 0

        for i, ch in enumerate(s1):
            index = ord(ch) - ord('a')
            arr[index] += 1
            ss1 += index

            if i == len(s1) - 1:
                break

            ch2 = s2[i]
            index2 = ord(ch2) - ord('a')
            arr2[index2] += 1
            ss2 += index2

        for i in range(len(s1) - 1, len(s2)):
            index = ord(s2[i]) - ord('a')
            arr2[index] += 1
            ss2 += index

            if ss1 == ss2:
                ok = True
                for ii, each in enumerate(arr):
                    if arr2[ii] != each:
                        ok = False

                if ok:
                    return True

            j = i - len(s1) + 1
            index = ord(s2[j]) - ord('a')
            ss2 -= index

            arr2[index] -= 1

        return False


s = Solution()
a = s.checkInclusion("abcd", "dbac")
print(a)

# l1 = 1
# l1 == l2
# 


