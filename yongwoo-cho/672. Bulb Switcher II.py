class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if m == 0 :
            return 1
        if n >= 3:
            if m == 0:
                return 1
            elif m == 1:
                return 4
            elif m == 2:
                return 7
            
            elif m >=3:
                return 8
        
        else:
            if n == 0 :
                return 1
            elif n == 1:
                return 2
            elif n == 2:
                if m == 1:
                    return 3
                else:
                    return 4
            
                
