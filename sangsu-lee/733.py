from typing import List
from copy import deepcopy

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        len_row = len(image)
        len_col = len(image[0])
        start_color = image[sr][sc]
        visited = [[0 for _ in range(len_col)] for _ in range(len_row)]
        q = [[sr, sc]]
        while q:
            r, c = q.pop(0)
            visited[r][c] = 1
            image[r][c] = newColor
            for dr, dc in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                tr, tc = r+dr, c+dc
                if tr < len_row and tr >= 0 and tc < len_col and tc >= 0 and image[tr][tc] == start_color and not visited[tr][tc]:
                    image[tr][tc] = newColor
                    q.append([tr, tc])
        return image

s = Solution()
print(s.floodFill([[0,0,0],[0,1,1]], 1, 1, 1))
print(s.floodFill([[0,0,0],[0,0,0]], 0, 0, 2))
