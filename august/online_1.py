
class Solution:
    def find(self, N, M, A, B) -> int:
        if N == 1:
            return 0 if A[0] in B else 1

        # minv = float("inf")

        noadd, add = float("inf"), float("inf")
        noadd = self.find(N - 1, M, A[1:], B) + 1

        temp = A[0]

        for m in range(M):
            if B[m] == temp:
                add = min(add, self.find(N - 1, M - m - 1, A[1:], B[m+1:]))

        return min(noadd, add)

s = Solution()

a = [2, 4, 5, 6, 7, 8, 9, 12, 14, 15, 19, 20, 21, 26, 30]
b = [2, 6, 6, 23, 9, 2, 14, 27, 17, 20, 24, 23, 16, 19, 16, 17, 11, 29]

a = [1, 3, 4, 8, 9, 14, 16, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29, 30]
b = [2, 25, 25, 9, 11, 5, 7, 18, 13, 6, 2, 24, 16, 17, 27, 9, 12]

a = [3, 5, 6, 7, 9, 11, 13, 14, 15, 16, 17, 19, 23, 24, 26, 30]
b = [6, 26, 2, 25, 26, 5, 20, 23]

resp = s.find(len(a), len(b), a, b)
print(resp)


