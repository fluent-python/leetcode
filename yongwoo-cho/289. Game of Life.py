import copy
class Solution:
    def interact(self, board,x ,y):
        sum_inter = 0
        if x - 1 >= 0 :
            sum_inter += board[x-1][y]
            if y - 1 >= 0:
                sum_inter += board[x-1][y-1]
            if y + 1  < len(board[0]):
                sum_inter += board[x-1][y+1]
                
        if y - 1 >= 0:
            sum_inter += board[x][y-1]
        if y + 1  < len(board[0]):
            sum_inter += board[x][y+1]
        
        if x + 1 < len(board) :
            sum_inter += board[x+1][y]
            if y - 1 >= 0:
                sum_inter += board[x+1][y-1]
            if y + 1  < len(board[0]):
                sum_inter += board[x+1][y+1]   
        return sum_inter
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = copy.deepcopy(board)
        
        for x in range(len(new_board)):
            for y in range(len(new_board[0])):
                inter_score = self.interact(new_board,x,y)
                print(x,y,inter_score)
                if new_board[x][y] == 0:
                    if inter_score == 3:
                        board[x][y] = 1
                else:
                    if (inter_score == 2) or (inter_score == 3):
                        board[x][y] = 1
                    else:
                        board[x][y] = 0
        
