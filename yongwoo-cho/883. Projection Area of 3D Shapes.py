class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top_prj = 0
        front_prj = grid[0]
        side_prj = 0
        
        for line in grid:
            print(max(line))
            side_prj += max(line)
            for idx, value in enumerate(line):
                if value != 0:
                    top_prj += 1
                if front_prj[idx] < value:
                    front_prj[idx] = value
        
        return sum(front_prj) + top_prj + side_prj
            
        
