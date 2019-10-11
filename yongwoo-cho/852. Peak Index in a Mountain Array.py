class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        pos = 0
        before = A[0]
        result = 0 
        
        for enum, a in enumerate(A[1:]):
            if before < a:
                result = enum+1
            if before > a:
                return result
            before = a
    
                
            
            
        
        
