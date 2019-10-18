tri_mem = {0: 0, 1: 1, 2: 1}
class Solution:
    def tribonacci(self, n: int) -> int:    
        
        def tri(n):
            global tri_mem
            if n not in tri_mem :
                tri_mem[n] =  tri(n-3)+ tri(n-2) + tri(n-1)      
            return tri_mem[n]  
        return tri(n)
        
