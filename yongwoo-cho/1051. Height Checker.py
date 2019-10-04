class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h_sort = heights.copy()
        h_sort.sort()
        result = 0 
        for i, j in zip(h_sort,heights):
            if i != j:
                result +=1 
        
        return result
            
            
            
