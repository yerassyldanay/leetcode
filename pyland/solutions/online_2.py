from typing import List

class Solution:
    def __init__(self):
        self.mv = [float("-inf"), float("-inf")]

    def xor(self, mat: List[List[int]], k: int) -> int:
        if not mat:
            return 0

        N = len(mat)
        M = len(mat[0])

        row = [0 for _ in range(M)]
        xmat = [row.copy() for _ in range(N)]

        for n in range(N):
            for m in range(M):
                if m == 0:
                    xmat[n][m] = mat[n][m]
                else:
                    xmat[n][m] = xmat[n][m - 1] ^ mat[n][m]

        for n in range(1, N):
            for m in range(M):
                xmat[n][m] = xmat[n - 1][m] ^ xmat[n][m]

        # print(xmat)

        return self.kth_element(xmat, k)

    def kth_element(self, mat: List[List[int]], k):
        arr = []
        for row in mat:
            arr.extend(row)

        arr = sorted(arr, key=lambda x: -x)

        # print(arr)

        return arr[k - 1]

s = Solution()
a = s.xor([[1, 2, 3], [2, 3, 2]], 4)
print(a)