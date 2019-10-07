class Solution:
    def checkRecord(self, s: str) -> bool:
        total_A = 0
        continuous_L = 0 
        for i in s:
            if i == "L":
                continuous_L += 1
            else:
                continuous_L = 0
            
            if i =="A":
                total_A += 1
            
            if total_A > 1 or continuous_L > 2:
                return False
        
        return True
            
            
            
