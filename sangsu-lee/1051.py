from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        bool_list = [0 if x == y else 1 for x, y in zip(heights, sorted_heights)]
        return sum(bool_list)

s = Solution()
s.heightChecker([1, 1, 4, 2, 1, 3])
