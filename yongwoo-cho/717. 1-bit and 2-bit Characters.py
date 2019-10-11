class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        
        stacked = 0
        for bit in bits[:-1]:
            if bit == 1:
                if stacked == 0:
                    stacked = 1
                elif stacked == 1:
                    stacked = 0
            
            elif bit == 0:
                if stacked == 1:
                    stacked = 0
                    
        if stacked == 1:
            return False
        
        return True
                    
                
