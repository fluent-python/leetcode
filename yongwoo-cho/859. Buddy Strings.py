from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        diff_index = [] 
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_index.append(i)
        
        if len(diff_index) == 0:
            for i in Counter(A).values():
                if i%2 == 0:
                    return True
            else:
                return False
                
                
        if len(diff_index) != 2:
            return False
        else :
            if (A[diff_index[0]] == B[diff_index[1]]) & (A[diff_index[1]] == B[diff_index[0]]):
                return True
        return False
            
                
            
        
        
