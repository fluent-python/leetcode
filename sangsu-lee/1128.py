from typing import List
import operator as op
from functools import reduce

class Solution:
    def nCr(self, n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer / denom

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        for domino in dominoes:
            d_sorted = sorted(domino)
            if not str(d_sorted) in d:
                d[str(d_sorted)] = 1
            else:
                d[str(d_sorted)] += 1

        ans = 0
        for k, v in d.items():
            if v >= 2:
                ans += int(self.nCr(v, 2))
        return ans


s = Solution()
print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(s.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
