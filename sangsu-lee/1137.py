dp = [-1 for _ in range(40)]
dp[0] = 0
dp[1] = 1
dp[2] = 1
class Solution:

    def tribonacci(self, n: int) -> int:
        global dp
        if dp[n] != -1:
            return dp[n]
        ans = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        dp[n] = ans
        return ans
