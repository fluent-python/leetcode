from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = N % 14 if N % 14 != 0 else 14

        for day in range(N):
            result = [0] * len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    result[i] = 1
                else:
                    result[i] = 0
            cells = result
        return cells


if __name__ == '__main__':
    res = Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7)
    print(res)