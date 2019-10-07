class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        m = -1
        while n > 0 :
            if m == - 1:
                m = n % 2
            elif n % 2 == m :
                return False
            m = n % 2
            n = n//2
        
        return True
            
