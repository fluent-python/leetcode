from typing import List
from copy import deepcopy

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        sum_orig = sum([sum(row) for row in grid])
        leftmaxes = [max(row) for row in grid]
        bottomMaxes = [max(x) for x in zip(*grid)]
        left_tups = [(i, 'left', x) for i, x in enumerate(leftmaxes)]
        bottom_tups = [(i, 'bottom', x) for i, x in enumerate(bottomMaxes)]
        all_tups = left_tups + bottom_tups
        all_tups.sort(key=lambda x: x[2])
        new_board = [[-1 for _ in range(len(grid))] for _ in range(len(grid))]
        for i, direction, val in all_tups:
            if direction == 'left':
                for j in range(len(grid)):
                    if new_board[i][j] == -1:
                        new_board[i][j] = val
            else:
                for j in range(len(grid)):
                    if new_board[j][i] == -1:
                        new_board[j][i] = val
        sum_inc = sum([sum(row) for row in new_board])
        return sum_inc - sum_orig

s = Solution()
sol = s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
print(sol)

