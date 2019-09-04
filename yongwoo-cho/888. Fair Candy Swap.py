class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        gap = int((sum(B) - sum(A))/2)
        sA = set(A)
        for b in B:
            if (b - gap) in sA:
                return [b-gap,b]
  
        
        
