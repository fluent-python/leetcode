class Solution:
    def binaryGap(self, N: int) -> int:
        binary = bin(N)[2:]
        before  = -1
        result = 0
        for enum,  i in enumerate(binary[::-1]):
            if i == "1":
                pos = len(binary) - enum -1 
                if before == -1 :
                    before = pos
                elif before - pos > result:
                    result = before -pos
                before = pos
        
        return result
            
                
            
                
                
                
            
                
     
            
            
            
                
                
