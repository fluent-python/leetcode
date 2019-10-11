class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # L >= W
        # L - W must be minimum
        N = int(math.sqrt(area))
        while N > 1: 
            if area % N == 0 :
                return [area // N, N]
            else:
                N -= 1
        return [area, 1]
                
