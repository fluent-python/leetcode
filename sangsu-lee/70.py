import math

class Solution:

    def nCr(self, n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

    def climbStairs(self, n: int) -> int:
        start = math.ceil(n / 2.)
        _r = 0 if n % 2 == 0 else 1
        end = n + 1
        answer = 0

        for x in range(start, end):
            answer += self.nCr(x, _r)
            _r += 2

        return int(answer)
