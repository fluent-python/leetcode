class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        result = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 :
                    result += 2
                for move in range(4):
                    if 0 <= i+dx[move] <len(grid) and 0 <= j+dy[move] < len(grid[0]):
                        calc = grid[i][j] - grid[i+dx[move]][j+dy[move]] 
                        if calc > 0 :
                            result += calc
                    else:
                        result += grid[i][j]
        
        return result
