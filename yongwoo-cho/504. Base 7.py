class Solution:
    def convertToBase7(self, num: int) -> str:
        minus = 0
        if num < 0 :
            minus = 1
            num = num * (-1)
        
        result = []
        if num == 0:
            return "0"
        while num > 0 :
            result.insert(0,str(num % 7))
            num = num // 7
            
        if minus == 1:
            result.insert(0, "-")
        
        return "".join(result)
        
        
            
            
            
            
            
