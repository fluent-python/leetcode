class Solution:
    def isUgly(self, num: int) -> bool:
        remainder = 0
        if num == 0 :
            return False
        for pos in [2,3,5]:
            while remainder == 0:
                remainder = num % pos
                num = num /pos
            num = num * pos
            remainder = 0 
            if num == 1:
                return True
        return False
                
                
