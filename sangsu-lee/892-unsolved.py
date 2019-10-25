from typing import List
import itertools as it

# 처음엔 3곳만 보면 되는줄 알았는데 역시아님
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        grid_transposed = [*zip(*grid)]
        flattened = list(it.chain(*grid))
        z = 2*(len(flattened) - flattened.count(0))
        x = 2*(sum([max(li) for li in grid]))
        y = 2*(sum([max(li) for li in grid_transposed]))
        print("x: {}, y: {}, z: {}".format(x, y, z))
        return x + y + z

s = Solution()

print(s.surfaceArea([[2]]))
print(s.surfaceArea([[1,2],[3,4]]))
print(s.surfaceArea([[1,0],[0,2]]))
print(s.surfaceArea())
print(s.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
