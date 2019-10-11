class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        min_count = zero_to_one = S.count("0")
        one_to_zero = 0 
          
        for s in S:
            if s == "0":
                zero_to_one -=1
            elif s == "1":
                one_to_zero +=1
            
            if min_count  > (zero_to_one + one_to_zero):
                min_count = zero_to_one + one_to_zero
        
        return min_count
        
        
