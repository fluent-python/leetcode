class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1, 1]
        i = 0
        while i < n - 1:
            memo.append(memo[i] + memo[i + 1])
            i += 1
        return memo[-1]