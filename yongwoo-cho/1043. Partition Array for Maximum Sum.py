class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        def maxSum(A,K):
            if len(A) == 1:
                return A[0]
            elif len(A) == 0:
                return 0
            
            for i in range(1,K+1):
                
                
            
            return max(maxSum(A[1:],K) +A[0],maxSum(A[2:],K)+max(A[0],A[1])*2, maxSum()
        
        
