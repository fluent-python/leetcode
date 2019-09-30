from typing import List
import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        new_board = copy.deepcopy(board)

        for x, row in enumerate(board):
            for y, item in enumerate(row):
                lives = self.get_live_neighbours_count(board, x, y)
                if lives = 3

    def get_live_neighbours_count(self, board, x, y):
        cnt = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    # print("cur_x: {}, cur_y: {}. continue".format(x+dx, y+dy))
                    continue
                if x + dx < 0 or x + dx >= len(board[0]) or y + dy < 0 or y + dy >= len(board):
                    # print("cur_x: {}, cur_y: {}. continue".format(x+dx, y+dy))
                    continue
                if board[y+dy][x+dx] == 1:
                    # print("cur_x: {}, cur_y: {}. count".format(x+dx, y+dy))
                    cnt += 1
        return cnt



s = Solution()

s.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])
