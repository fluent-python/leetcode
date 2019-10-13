class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_result = 0 
        visited = []
        for _ in range(len(grid)):
            visited.append([0] * len(grid[0]))

        # can move 
        def dfs(i,j):
            visited[i][j] = 1
            count = 1
            move = [[-1,0],[1,0],[0,-1],[0,1]]
            for m in move:

                if 0 <= (i+m[0]) < len(grid) and 0 <= (j+m[1]) < len(grid[0]):
                    if grid[i+m[0]][j+m[1]] == 1 and visited[i+m[0]][j+m[1]] == 0:
                        count += dfs(i+m[0],j+m[1])
            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    result = dfs(i,j)
                    if max_result < result:
                        max_result = result
        
        return max_result
