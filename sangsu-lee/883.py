from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        xy = sum([len([item for item in li if item]) for li in grid])
        # enumerate X, max Y
        xz = sum([max(ys) for ys in grid])
        tp_grid = list(map(list, zip(*grid)))
        yz = sum([max(xs) for xs in tp_grid])

        return sum([xy, xz, yz])


s = Solution()
print(s.projectionArea([[1, 2], [3, 4]]))
print(s.projectionArea([[1,0],[0,2]]))
