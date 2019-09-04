from typing import List
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        asum, bsum = sum(A), sum(B)
        # A - B
        sub = asum - bsum
        for a in A:
            for b in B:
                if (a - b)*2 == sub:
                    return [a, b]

s = Solution()
print(s.fairCandySwap([1, 2, 5], [2, 4]))

