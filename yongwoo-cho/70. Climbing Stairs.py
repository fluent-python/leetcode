def fac(n: int) :
    fac = 1
    for i in range(2, n+1):
        fac *= i
    return fac
class Solution:
    def climbStairs(self, n: int) -> int:
        max_2 = n//2
        count = 0
        min_1 = n %2
        
        if n == 1 :
            return 1
        
        for i in range(0,max_2+1):
            num_of_1 = (n-i*2)
            num_of_2 = i
            count += fac(num_of_1+num_of_2) / (fac(num_of_1) * fac(num_of_2))
       
    
        return int(count)    
