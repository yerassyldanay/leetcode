
def isPrime(n: int):
    if n <= 1:
        return False
    elif n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    f = 5
    while f * f <= n:
        if n % f == 0:
            return False
        f = f + 1

    return True


class Solution(object):
    def numSquares(self,n):
        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = min([dp[i-j*j] for j in range(1,int(i**.5)+1)])+1
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(90))